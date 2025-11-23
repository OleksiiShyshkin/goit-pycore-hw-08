from __future__ import annotations
from collections import UserDict
import re
from typing import List, Optional
from datetime import datetime, date, timedelta


class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value: str):
        v = (value or "").strip()
        if not v:
            raise ValueError("Name cannot be empty.")
        super().__init__(v)


class Phone(Field):
    _re = re.compile(r"^\d{10}$")

    def __init__(self, value: str):
        v = (value or "").strip()
        if not Phone._re.fullmatch(v):
            raise ValueError("Phone must be exactly 10 digits.")
        super().__init__(v)

class Birthday(Field):
    def __init__(self, value: str):
        v = (value or "").strip()
        try:
            datetime.strptime(v, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(v)

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.birthday: Optional[Birthday] = None

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def find_phone(self, phone: str) -> Optional[Phone]:
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone: str) -> None:
        target = self.find_phone(phone)
        if not target:
            raise ValueError("Phone not found.")
        self.phones.remove(target)

    def edit_phone(self, old_phone: Optional[str], new_phone: str) -> None:
        if old_phone is None:
            if len(self.phones) == 1:
                replacement = Phone(new_phone)
                self.phones[0].value = replacement.value
                return
            raise ValueError("Specify old phone explicitly when contact has 0 or more than 1 phone.")

        target = self.find_phone(old_phone)
        if not target:
            raise ValueError("Old phone not found.")
        replacement = Phone(new_phone)
        target.value = replacement.value

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones) if self.phones else "—"
        birthday = self.birthday.value if self.birthday else "—"
        return f"Contact name: {self.name.value}, birthday: {birthday}, phones: {phones}"


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self) -> List[dict]:
        today = date.today()
        end_date = today + timedelta(days=7)
        result: List[dict] = []

        for record in self.data.values():
            if not record.birthday:
                continue

            original = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
            birthday_this_year = original.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            if today <= birthday_this_year <= end_date:
                congrats_date = birthday_this_year

                if congrats_date.weekday() == 5:
                    congrats_date += timedelta(days=2)
                elif congrats_date.weekday() == 6:
                    congrats_date += timedelta(days=1)

                result.append(
                    {
                        "name": record.name.value,
                        "birthday": congrats_date.strftime("%d.%m.%Y"),
                    }
                )

        result.sort(
            key=lambda x: datetime.strptime(x["birthday"], "%d.%m.%Y").date()
        )
        return result

    def __str__(self) -> str:
        if not self.data:
            return "AddressBook is empty."
        lines = [str(self.data[k]) for k in sorted(self.data.keys())]
        return "\n".join(lines)
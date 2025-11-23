from typing import List
from errors import input_error
from models import AddressBook, Record


@input_error
def handle_add(args: List[str], book: AddressBook) -> str:
    if len(args) != 2:
        raise ValueError("Give me name and phone please.")
    name, phone = args
    rec = book.find(name)
    if rec is None:
        rec = Record(name)
        rec.add_phone(phone)
        book.add_record(rec)
        return "Contact added."
    else:
        rec.add_phone(phone)
        return "Phone added to existing contact."


@input_error
def handle_change(args: List[str], book: AddressBook) -> str:
    if len(args) not in (2, 3):
        raise ValueError("Give me name and new phone please (or name old_phone new_phone).")
    name = args[0]
    rec = book.find(name)

    if len(args) == 2:
        _, new_phone = args
        rec.edit_phone(old_phone=None, new_phone=new_phone)
    else:
        _, old_phone, new_phone = args
        rec.edit_phone(old_phone=old_phone, new_phone=new_phone)
    return "Contact updated."


@input_error
def handle_phone(args: List[str], book: AddressBook) -> str:
    if len(args) != 1:
        raise ValueError("Enter user name.")
    name = args[0]
    rec = book.find(name)

    if not rec.phones:
        return "No phones."
    return "; ".join(p.value for p in rec.phones)


@input_error
def handle_all(_: List[str], book: AddressBook) -> str:
    return str(book)


@input_error
def handle_delete(args: List[str], book: AddressBook) -> str:
    if len(args) != 1:
        raise ValueError("Enter user name to delete.")
    name = args[0]
    rec = book.find(name)
    _ = rec.name
    book.delete(name)
    return "Contact deleted."


@input_error
def handle_addphone(args: List[str], book: AddressBook) -> str:
    if len(args) != 2:
        raise ValueError("Give me name and phone please.")
    name, phone = args
    rec = book.find(name)
    if rec is None:
        raise KeyError
    rec.add_phone(phone)
    return "Phone added."


@input_error
def handle_removephone(args: List[str], book: AddressBook) -> str:
    if len(args) != 2:
        raise ValueError("Give me name and phone to remove.")
    name, phone = args
    rec = book.find(name)
    rec.remove_phone(phone)
    return "Phone removed."


@input_error
def handle_find(args: List[str], book: AddressBook) -> str:
    if len(args) != 1:
        raise ValueError("Enter user name to find.")
    name = args[0]
    rec = book.find(name)
    _ = rec.name
    return str(rec)


@input_error
def handle_add_birthday(args: List[str], book: AddressBook) -> str:
    if len(args) != 2:
        raise ValueError("Give me name and birthday please (DD.MM.YYYY).")
    name, birthday = args
    rec = book.find(name)
    rec.add_birthday(birthday)
    return "Birthday added."


@input_error
def handle_show_birthday(args: List[str], book: AddressBook) -> str:
    if len(args) != 1:
        raise ValueError("Enter user name.")
    name = args[0]
    rec = book.find(name)
    if not rec.birthday:
        return "No birthday set."
    return rec.birthday.value


@input_error
def handle_birthdays(args: List[str], book: AddressBook) -> str:
    if args:
        raise ValueError("This command does not take any arguments.")
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    lines = [f"{item['name']}: {item['birthday']}" for item in upcoming]
    return "\n".join(lines)
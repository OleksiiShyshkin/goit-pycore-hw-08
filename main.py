from models import AddressBook
from utils import parse_input, help_text
from commands import (
    handle_add,
    handle_change,
    handle_phone,
    handle_all,
    handle_delete,
    handle_addphone,
    handle_removephone,
    handle_find,
    handle_add_birthday,
    handle_show_birthday,
    handle_birthdays,
)
from storage import load_data, save_data


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    print("Type 'help' to see available commands.")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            save_data(book)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            print(help_text())
        elif command == "add":
            print(handle_add(args, book))
        elif command == "change":
            print(handle_change(args, book))
        elif command == "phone":
            print(handle_phone(args, book))
        elif command == "all":
            print(handle_all(args, book))
        elif command == "delete":
            print(handle_delete(args, book))
        elif command == "addphone":
            print(handle_addphone(args, book))
        elif command == "removephone":
            print(handle_removephone(args, book))
        elif command == "find":
            print(handle_find(args, book))
        elif command == "add-birthday":
            print(handle_add_birthday(args, book))
        elif command == "show-birthday":
            print(handle_show_birthday(args, book))
        elif command == "birthdays":
            print(handle_birthdays(args, book))
        else:
            print("Invalid command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()

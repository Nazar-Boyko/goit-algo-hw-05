from typing import Callable


def input_error(func: Callable) -> Callable:
    """
    Декоратор для обробки помилок введення користувача.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
    return inner


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Розбирає введення користувача на команду та аргументи.
    """
    parts = user_input.split()

    if not parts:
        return "", []

    command, *args = parts
    return command.lower(), args


@input_error
def add_contact(args: list[str], contacts: dict) -> str:
    """
    Додає новий контакт.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list[str], contacts: dict) -> str:
    """
    Змінює номер існуючого контакту.
    """
    name, phone = args

    if name not in contacts:
        raise KeyError

    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args: list[str], contacts: dict) -> str:
    """
    Показує номер контакту.
    """
    name = args[0]

    return contacts[name]


@input_error
def show_all(_: list[str], contacts: dict) -> str:
    """
    Показує всі контакти.
    """
    if not contacts:
        return "No contacts found."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    """
    Основна функція запуску бота.
    """
    contacts: dict[str, str] = {}

    print("Welcome to assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
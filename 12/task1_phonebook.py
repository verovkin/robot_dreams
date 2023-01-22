"""
Home Work 11
Dmytro Verovkin
robot_dreams

1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.

Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
Підказка: Ви можете використати бібліотеку json, яка допоможе із перетворенням dict в JSON string (при записі в файл)
і JSON string в dict (при читанні із файлу). Файл слід оновлювати після кожної успішної операції add або delete.
"""

import json

print("PHONE BOOK")
print("commands: stats, add <name> <phone>, delete <name>, list, show <name>, exit, help")
help_text = """
--------------------------------------------------------------------------------------------------
PHONEBOOK HELP

Use commands to operate this phonebook.json:
stats              - shows number of phonebook.json entries
add <name> <phone> - adds <name> and <phone> number to phonebook.json, if <name> is not already exists
show <name>        - prints name and phone number for entry <name>
delete <name>      - deletes entry from phonebook.json by <name>
list               - prints all entries of the phonebook.json
exit               - exits the program
help               - shows this help message
--------------------------------------------------------------------------------------------------
"""


PHONE_BOOK_BD_FILE = 'phonebook.json'

try:
    with open(PHONE_BOOK_BD_FILE, 'r') as f:
        phone_book = json.load(f)
except FileNotFoundError:
    phone_book = {}


def get_stat():
    print(f"Total {len(phone_book)} entries")


def add_to_phonebook(name, phone):
    if name in phone_book:
        return False
    else:
        phone_book[name] = phone
        with open(PHONE_BOOK_BD_FILE, 'w') as f:
            json.dump(phone_book, f)
        return True


def delete_from_phonebook(name):
    if name not in phone_book:
        return False
    else:
        del phone_book[name]
        with open(PHONE_BOOK_BD_FILE, 'w') as f:
            json.dump(phone_book, f)
        return True


def list_all_from_phonebook():
    if len(phone_book) > 0:
        for key, value in phone_book.items():
            print(f"{key} {value}")
    else:
        print("empty")


def show_from_phonebook(name):
    print(f"{name} {phone_book[name] if name in phone_book else 'not found'}")


while True:
    user_input = input("Make your input: ")

    if len(user_input) < 1:  # check if user input is not empty
        print("Please enter command")
        continue

    user_input_split = user_input.split()

    match user_input_split[0]:
        case 'stats':
            get_stat()
        case 'add':
            if len(user_input_split) == 3:  # check if user entered correct number of arguments
                if add_to_phonebook(user_input_split[1], user_input_split[2]):
                    print("Added successfully")
                else:
                    print(f"{user_input_split[1]} is already exist")
            else:
                print("Wrong arguments, please use format: add <name> <phone>")
        case 'delete':
            if len(user_input_split) == 2:  # check if user entered correct number of arguments
                if delete_from_phonebook(user_input_split[1]):
                    print(f"{user_input_split[1]} deleted")
                else:
                    print(f"{user_input_split[1]} is not found")
            else:
                print("Wrong arguments, please use format: delete <name>")
        case 'list':
            list_all_from_phonebook()
        case 'show':
            show_from_phonebook(user_input_split[1])
        case 'exit':
            break
        case 'help':
            print(help_text)
        case _:
            print("Unknown command")

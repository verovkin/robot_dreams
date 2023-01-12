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

from os import path

PHONE_BOOK_BD_FILE = 'phonebook.json'

# check if database file is exist. if not - create empty
if not path.exists(PHONE_BOOK_BD_FILE):
    with open(PHONE_BOOK_BD_FILE, 'w') as f:
        empty_phone_book = {}
        json_data = json.dumps(empty_phone_book)
        f.write(json_data)


def rewrite_JSONed(file, raw_data):
    """
    Converts RAW data into JSON and rewrites to an open file
    :param file:file instance
    :param raw_data: data to convert to JSON and save
    :return:
    """
    json_data = json.dumps(raw_data)
    file.truncate(0)
    file.seek(0)
    file.write(json_data)


def get_stat():
    with open(PHONE_BOOK_BD_FILE, 'r') as f:
        file_data = f.read()
        phone_book = json.loads(file_data)
        print(f"Total {len(phone_book)} entries")


def add_to_phonebook(name, phone):
    with open(PHONE_BOOK_BD_FILE, 'r+') as f:
        file_data = f.read()
        phone_book = json.loads(file_data)

        if name in phone_book:
            return False
        else:
            phone_book[name] = phone
            rewrite_JSONed(f, phone_book)
            return True


def delete_from_phonebook(name):
    with open(PHONE_BOOK_BD_FILE, 'r+') as f:
        file_data = f.read()
        phone_book = json.loads(file_data)

        if name not in phone_book:
            return False
        else:
            del phone_book[name]
            rewrite_JSONed(f, phone_book)
            return True


def list_all_from_phonebook():
    with open(PHONE_BOOK_BD_FILE, 'r') as f:
        file_data = f.read()
        phone_book = json.loads(file_data)

        if len(phone_book) > 0:
            for key, value in phone_book.items():
                print(f"{key} {value}")
        else:
            print("empty")


def show_from_phonebook(name):
    with open(PHONE_BOOK_BD_FILE, 'r') as f:
        file_data = f.read()
        phone_book = json.loads(file_data)
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

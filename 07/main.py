"""
Home Work 04
Dmytro Verovkin
robot_dreams


Створити телефонну книгу, яка матиме наступні команди:

stats: кількість записів
add: додати запис
delete <name>: видалити запис за іменем (ключем)
list: список всіх імен в книзі
show <name>: детальна інформація по імені

Записи не мають повторюватися, заборонено перезаписувати записи, тільки видаляти і додавати заново.
"""


print("PHONE BOOK")
print("commands: stats, add <name> <phone>, delete <name>, list, show <name>, exit, help")
help_text = """
--------------------------------------------------------------------------------------------------
PHONEBOOK HELP

Use commands to operate this phonebook:
stats              - shows number of phonebook entries
add <name> <phone> - adds <name> and <phone> number to phonebook, if <name> is not already exists
show <name>        - prints name and phone number for entry <name>
delete <name>      - deletes entry from phonebook by <name>
list               - prints all entries of the phonebook
exit               - exits the program
help               - shows this help message
--------------------------------------------------------------------------------------------------
"""

phone_book = {}

while True:
    user_input = input("Make your input: ")

    if len(user_input) < 1:             # check if user input is not empty
        print("Please enter command")
        continue

    user_input_split = user_input.split()

    match user_input_split[0]:
        case 'stats':
            print(f"Total {len(phone_book)} entries")
        case 'add':
            # check if user entered correct number of arguments
            if len(user_input_split) == 3:
                # check if name is not in phonebook
                if user_input_split[1] not in phone_book:
                    phone_book[user_input_split[1]] = user_input_split[2]
                    print("Added successfully")
                else:
                    print(f"{user_input_split[1]} is already exist")
            else:
                print("Wrong arguments, please use format: add <name> <phone>")
        case 'delete':
            # check if user entered correct number of arguments
            if len(user_input_split) == 2:
                # check if name is in phonebook
                if user_input_split[1] in phone_book:
                    del phone_book[user_input_split[1]]
                    print(f"{user_input_split[1]} deleted")
                else:
                    print(f"{user_input_split[1]} is not found")
            else:
                print("Wrong arguments, please use format: delete <name>")
        case 'list':
            # check if phonebook has entries
            if len(phone_book) > 0:
                for key, value in phone_book.items():
                    print(f"{key} {value}")
            else:
                print("empty")
        case 'show':
            if phone_book.get(user_input_split[1]) is not None:
                print(f"{user_input_split[1]} {phone_book[user_input_split[1]]}")
            else:
                print(f"{user_input_split[1]} not found")
        case 'exit':
            break
        case 'help':
            print(help_text)
        case _:
            print("Unknown command")


"""
Home Work 04
Dmytro Verovkin
robot_dreams


Створити програму, яка буде очікувати від користувача введення тексту і виведе
інформацію по кожному надрукованому символу:

це “число” + яке воно (парне, непарне),
це “буква” + яка вона (велика чи маленька),
це “символ”
"""


text = input("Enter your text: ")

for char in text:
    if char.isdigit():
        if int(char) % 2 == 0:
            print(f"{char} - is a EVEN number")
        else:
            print(f"{char} - is a ODD number")
    elif char.isalpha():
        if char.islower():
            print(f"{char} - is a lowercase letter")
        else:
            print(f"{char} - is a uppercase letter")
    else:
        print(f"{char} - is a symbol")

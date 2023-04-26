"""
Home Work 14 task 2
Dmytro Verovkin
robot_dreams

2. (необов'язкове виконання) Написати програму, яка буде:
зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)x
знаходити всі email в тексті і змінювати їх на *@*.

"""


from os import path
import re
import sys

# if user not entered argument - ask to input filename
if len(sys.argv) < 2:
    txt_file = input("Enter filename: ")
else:
    txt_file = sys.argv[1]

# check if file exist:
if not path.exists(txt_file):
    print(f"File '{txt_file}' not found")
    exit()

with open(txt_file, 'r') as f:
    text = f.read()

email_regex = r'(?![_.-])((?![_.-][_.-])[a-zA-Z\d_.-]){0,63}[a-zA-Z\d]@((?!-)((?!--)[a-zA-Z\d-]){0,63}[a-zA-Z\d]\.){1,2}([a-zA-Z]{2,14}\.)?[a-zA-Z]{2,14}'
# email_regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
x = re.sub(email_regex, '*@*', text)
print(x)

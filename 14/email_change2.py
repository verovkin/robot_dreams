"""
Home Work 14 task 3
Dmytro Verovkin
robot_dreams

3. (необов'язкове виконання) Написати програму, яка буде:
зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
знаходити всі email в тексті і змінювати їх на X***@****X, де замість Х мають бути перша і остання літери
справжньої адреси, а весь інший текст має бути замінений на *. Кількість * необовʼязково
має відповідати кількості замінених символів
"""


from os import path
import re
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('filename')
# args = parser.parse_args()

# txt_file = args.filename
txt_file = 'email'

email_regex = re.compile(r'(?<=.).(?=[^@]*?@)|(?:(?<=@)|(?!^)(?=[^@]*$))(.)(?=.*\.)|(?:(?<=\.)(?=[^.]+$)|(?!^)(?=[^@.]*$))[^.](?!$)', re.MULTILINE)


# check if file exist:
if not path.exists(txt_file):
    print(f"File '{txt_file}' not found")
    exit()


with open(txt_file, 'r') as f:
    text = f.read()
print(text)
print()

email_regex = r'(?<=.)((?![_.-])((?![_.-][_.-])[a-zA-Z\d_.-]){0,63}[a-zA-Z\d]@((?!-)((?!--)[a-zA-Z\d-]){0,63}[a-zA-Z\d]\.){1,2}([a-zA-Z]{2,14}\.)?[a-zA-Z]{2,14}?(?=.))'
x = re.sub(email_regex, '***@****', text)
print(x)
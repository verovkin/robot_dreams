'''
Home Work_03
Dmytro Verovkin
'''

def main():

	# 1. Використовуючи функцію print, надрукувати фразу “I love Python” 42 рази.
	print("I love Python\n" * 42)

	# 2. Створити змінну age_in_month, надавши їй значення вашого поточного віку в місяцях.
	age_in_month = 39 * 12 + 8	# значення вашого поточного віку в місяцях. 

	# 3. Створити змінну age_in_years, в яку записати ваш вік в роках на основі попередньої змінної.
	# Підказка: використовуючи арифметичні оператори та/або приведення типів).
	age_in_years = age_in_month // 12  # вік в роках на основі попередньої змінної

	# 4. Створити змінну my_age, яка буде містити рядок “Му name is … I’m … years old”, де на 
	# замість пропусків буде підставлятись ваші імʼя та вік. Значення віку слід брати зі змінної age_in_years. 
	my_age = f"Му name is Dmitry, I’m {age_in_years} years old"

	# 5. Створити змінну зі значенням 1. Використовуючи оператори порівняння, порівняти її 
	# із будь-якими іншими значеннями (мінімум 5 порівнянь) і перевірити вивід в інтерпретаторі.
	num_one = 1
	print(f'{num_one}  > 0     is {num_one > 0}')
	print(f'{num_one} <= 2.2   is {num_one <= 2.2}')
	print(f'{num_one} == 1     is {num_one == 1}')
	print(f"{num_one} != 'abc' is {num_one != 'abc'}")
	print(f'{num_one} == 1.0   is {num_one == 1.0}')
	print()

	# 6. Створити змінні a=2, b=5, c=6. На основі цих змінних створити змінну d, значення якої має бути “256”
	a, b, c = 2, 5, 6
	d = str(a)+str(b)+str(c)
	print(d)


if __name__ == '__main__':
	main()
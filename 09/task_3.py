"""
Home Work 09 - task 3
Dmytro Verovkin
robot_dreams

3. Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі,
використовуючи рекурсію (необов'язкове виконання).
"""


def recursion_fibonacci(i, a=0, b=1, counter=0):
    if i == counter:
        return a
    return recursion_fibonacci(i, a=b, b=a+b, counter=counter + 1)


while True:
    user_input = input("Enter index number of Fibonacci sequence: ")
    try:
        index = int(user_input)
    except ValueError:
        print("Enter integer number!")
        continue
    if index < 0:
        print("Enter positive number!")
        continue
    break

print(f"Fibonacci number with index {index} is {recursion_fibonacci(index)}")

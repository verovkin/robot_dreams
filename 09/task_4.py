"""
Home Work 09 - task 3
Dmytro Verovkin
robot_dreams

4. Написати програму, яка буде повертати факторіал введеного числа, використовуючи рекурсію
(необов'язкове виконання).
"""


def get_factorial(n):
    if n == 0:
        return 1
    return n * get_factorial(n - 1)


while True:
    user_input = input("Lets count factorial for number: ")
    try:
        index = int(user_input)
    except ValueError:
        print("Enter integer number!")
        continue
    if index < 0:
        print("Enter positive number!")
        continue
    break


print(f"{index}! is {get_factorial(index)}")

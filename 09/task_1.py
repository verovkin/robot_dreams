"""
Home Work 09 - task 1
Dmytro Verovkin
robot_dreams

1. Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі,
використовуючи генератори.
"""


def generator_fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def get_fibonacci_element_by_index(i):
    # increasing i to get element 0 with index 0
    i += 1
    answer = None
    for item in generator_fibonacci(i):
        answer = item
    return answer


# user input with validation for positive integer
while True:
    user_input = input("Enter index number of Fibonacci sequence: ")
    try:
        num_index = int(user_input)
    except ValueError:
        print("Enter integer number!")
        continue
    if num_index < 0:
        print("Enter positive number!")
        continue
    break


number = get_fibonacci_element_by_index(num_index)
print(f"Fibonacci number with index {num_index} is {number}")

"""
Home Work 09 - task 2
Dmytro Verovkin
robot_dreams

2. Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі,
використовуючи ітератори (необов'язкове виконання).
"""


class FibonacciIterator:
    def __init__(self, i):
        self.counter = 0
        self.index = i + 1  # + 1 for first fibonacci sequence element to have index number 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.index:
            raise StopIteration()
        tmp_val = self.a
        self.counter += 1
        self.a, self.b = self.b, self.a + self.b
        return tmp_val


# user input with validation for positive integer
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

fibonaccies = FibonacciIterator(index)
for item in fibonaccies:
    number = item

print(f"Fibonacci number with index {index} is {number}")

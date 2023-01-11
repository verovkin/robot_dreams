"""
Home Work 11
Dmytro Verovkin
robot_dreams

Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків дорівнює перед виконанням
коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює.

У випадку виникнення будь-якої помилки вона має бути надрукована текстом, проте програма не має завершити своєї роботи.
"""


class MyContextManager():
    def __enter__(self):
        print('=' * 10)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is not None:
            print(exc_value)
        print('=' * 10)
        return True


with MyContextManager():
    print('some code is running')

with MyContextManager():
    print(1 / 0)

print("End of the program")

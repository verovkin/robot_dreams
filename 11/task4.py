"""
Home Work 11
Dmytro Verovkin
robot_dreams

Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж, що і менеджер контексту із попереднього завдання.
"""


def my_try_except_context_manager(func):
    try:
        print("=" * 10)
        func()
    except Exception as e:
        print(e)
    finally:
        print("=" * 10)


my_try_except_context_manager(lambda: print("some function"))
my_try_except_context_manager(lambda: print(1 / 0))

print("End of the program")

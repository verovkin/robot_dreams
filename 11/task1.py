"""
Home Work 11
Dmytro Verovkin
robot_dreams

Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
Декоратор має працювати для різних функцій однаково.
"""


from datetime import datetime

def my_decorator(func):
    def wrap(*args, **kwargs):
        print(f"'{func.__name__}' called at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        func(*args, **kwargs)       # calling a function
    return wrap

@my_decorator
def function_1():
    print(f"function 1 is working without args")

@my_decorator
def function_2(a, b):
    print(f"function 2 is working, a + b = {a + b}")


function_1()
function_2(1, 2)

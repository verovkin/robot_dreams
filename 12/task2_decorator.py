"""
Home Work 11
Dmytro Verovkin
robot_dreams

2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.
"""


from datetime import datetime
LOG_FILE_NAME = 'log.log'

def log_decorator(func):
    def wrap(*args, **kwargs):
        with open(LOG_FILE_NAME, 'a') as f:
            print(f"'{func.__name__}' called at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", file=f)
        res = func(*args, **kwargs)       # calling a function
        return res
    return wrap


@log_decorator
def function_1():
    print(f"function 1 is working without args")

@log_decorator
def function_2(a, b):
    print(f"function 2 is working, a + b = {a + b}")


@log_decorator
def function_with_return():
    return 'returning string'


function_1()
function_2(1, 2)
print(function_with_return())


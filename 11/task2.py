"""
Home Work 11
Dmytro Verovkin
robot_dreams

Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured".
"""


class MyCustomException(Exception):
    pass


raise MyCustomException('Custom exception is occurred')

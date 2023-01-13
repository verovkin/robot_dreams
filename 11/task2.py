"""
Home Work 11
Dmytro Verovkin
robot_dreams

Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured".
"""


class MyCustomException(Exception):
    def __init__(self, message="Custom exception is occurred"):
        self.message = message
        super().__init__(self.message)

raise MyCustomException

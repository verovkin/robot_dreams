"""
HomeWork 14 - task 3
Dmytro Verovkin
robot_dreams

3.(необов'язкове виконання) Створити клас MyStr(str), який має перевизначтити метод str таким чином,
щоб замість друку реального значення всі літери були переведені в верхній регістр:
"""

class MyStr(str):
    def __str__(self):
        # return super().__str__().upper()
        return self.upper()


my_str = MyStr('test')
print(my_str)
# >> > "TEST"

"""
Home Work 11
Dmytro Verovkin
robot_dreams

3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.
"""


from datetime import datetime
LOG_FILE_NAME = 'exception_log.log'

class MyCustomException(Exception):

    def __init__(self, message="Custom exception is occurred"):
        self.message = message
        with open(LOG_FILE_NAME, 'a') as f:
            print(f"{self.__class__.__name__} - {self.message} Error at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", file=f)
        super().__init__(self.message)


raise MyCustomException

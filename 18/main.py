"""
HomeWork 14 - tasks 1, 2
Dmytro Verovkin
robot_dreams
"""
import unittest


class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        super().__init__(name)
        self.url = url
        self.chat_id = chat_id

    def send_message(self, message):
        print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id



class MyTestClass(unittest.TestCase):
    def test_set_url(self):
        tester_bot = TelegramBot('TestName')
        self.assertEqual(tester_bot.url, None, "incorкect URL, should be None")
        tester_bot.set_url("test.com")
        self.assertEqual(tester_bot.url, "test.com", "URL could not be set")


    def test_set_chat_id(self):
        tester_bot = TelegramBot('TestName')
        self.assertEqual(tester_bot.chat_id, None, "incorect chat_id, should be None")
        tester_bot.set_chat_id("123")
        self.assertEqual(tester_bot.chat_id, "123", "chat_id could not be set")


if __name__ == '__main__':
    unittest.main()


# some_bot = Bot('Marvin')
# some_bot.say_name()
# >> "Marvin"

# some_bot.send_message("Hello")
# >> > "Hello"
#
# telegram_bot = TelegramBot('TestName', url='test.com', chat_id='123')
# telegram_bot.say_name()
# # >> > "TG"
#
# telegram_bot.send_message('Hello')
# # >> > "TG bot says Hello to chat None using None"
#
# telegram_bot.set_chat_id(1)
# telegram_bot.send_message('Hello')
# # >> > "TG bot says Hello to chat 1 using None"

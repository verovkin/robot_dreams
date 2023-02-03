"""
HomeWork 14 - task 5
Dmytro Verovkin
robot_dreams

5. (необов'язкове виконання) Створити клас Bot та TelegramBot із першого завдання за допомогою функції type
"""


def bot_init_function(self, name):
    self.name = name

def bot_say_name_function(self):
    print(self.name)

def bot_send_message_function(self, message):
    print(message)


Bot = type(
    'Bot',
    (),
    {
        '__init__': bot_init_function,
        'say_name': bot_say_name_function,
        'send_message': bot_send_message_function,
    }
)


def tg_bot_init_function(self, name, url=None, chat_id=None):
    super(type(self), self).__init__(name)
    self.url = url
    self.chat_id = chat_id

def tg_bot_send_message_function(self, message):
    print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")

def tg_bot_set_url_function(self, url):
    self.url = url

def tg_bot_set_chat_id_function(self, chat_id):
    self.chat_id = chat_id


TelegramBot = type(
    'TelegramBot',
    (Bot,),
    {
        '__init__': tg_bot_init_function,
        'send_message': tg_bot_send_message_function,
        'set_url': tg_bot_set_url_function,
        'set_chat_id': tg_bot_set_chat_id_function,
    }
)


some_bot = Bot('Marvin')
some_bot.say_name()
# >> "Marvin"

some_bot.send_message("Hello")
# >> > "Hello"

telegram_bot = TelegramBot("TG")
telegram_bot.say_name()
# >> > "TG"

telegram_bot.send_message('Hello')
# >> > "TG bot says Hello to chat None using None"

telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')
# >> > "TG bot says Hello to chat 1 using None"

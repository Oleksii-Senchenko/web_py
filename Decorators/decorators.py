def greet(name):
    return f"Hello, {name}"


def say_bye(name):
    return f"Good bye, {name}"


my_function = greet


# print(my_function("Vadym"))


def call_function(func, arg):
    return func(arg)


# print(call_function(my_function, "Ann"))
# print(call_function(say_bye, "Ann"))

def get_func(name_func):
    if name_func == "sum":
        return sum
    elif name_func == "len":
        return len


result_func = get_func("len")
# print(result_func([1, 2, 7]))

list_func = [sum, len, range]

dict_func = {
    "sun": sum,
    "len": len,
    "range": range
}


# print(list_func[2](5))


def outer_function(message):
    def inner_function():
        print(message)

    return inner_function


hello_function = outer_function("Hello")
bye_func = outer_function("Bye")


# hello_function()
# bye_func()
#
#
# lexus_tell_about_day_day = outer_function("My day was incredible")
#
# lexus_tell_about_day_day()

# def func():
#     pass
#
# def decorators(func):
#     pass


def my_decorator(func):
    def wrapper():
        print("Wrapper before function.")
        func()
        print("Wrapper after function.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello, world!")


# Це колесса
# say_hello = my_decorator(say_hello)
# say_hello()


import functools


def decorator_with_arg(arg1, arg2):
    """dec params"""

    def actual_decorator(func):
        """Actual decorator"""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Wrapper"""
            print(f"Decorator take arguments: {arg1}, {arg2}")
            func(*args, **kwargs)

        return wrapper

    return actual_decorator


@decorator_with_arg("Nihao", 3.141592)
def my_func(*list_args, **dict_args):
    """main function"""
    print("Function is done!")
    print(list_args)
    print(dict_args)


#
# my_func("M", 34, name="Karina", age=45)
#
#
# print(my_func.__name__)
# print(my_func.__doc__)

import functools
import time
import datetime
import random


def simple_logger_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.datetime.now().strftime("%H:%M:%S")}] Call function: {func.__name__}")
        result =  func(*args, **kwargs)
        print(f"[{datetime.datetime.now().strftime("%H:%M:%S")}] Function {func.__name__} end processing")
        return result
    return wrapper



@simple_logger_decorator
def add_number(digit1, digit2):
    print(f"Add two digits: {digit1} + {digit2}")
    return digit1 + digit2



@simple_logger_decorator
def sub_number(digit1, digit2):
    print(f"Sub two digits: {digit1} - {digit2}")
    return digit1 - digit2

#
# print(add_number(37, 73))
# print(30 * "-")
# print(sub_number(102, 45))

user_roles = ["admin", "user"]
current_role = ["user"]

def role_required(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if role in current_role:
                print(f"Access approved for {func.__name__}. Role: {role}")

                result =  func(*args, **kwargs)
                return result
            else:
                print(f"Access denied for {func.__name__}. Need role: {role}")
        return wrapper
    return decorator

@role_required("admin")
def delete_user(user_id):
    """Delete user from base"""
    print(f"User [{user_id}] has been deleted successfully")
    return True

@role_required("user")
def view_profile(user_id):
    """View profile of user"""
    print(f"Current user look on profile: {user_id}")
    return True

# delete_user(777)
# current_role.append("admin")
# delete_user(678)
# view_profile(111)




class TelegramBot:
    _BOT_COMMANDS = {}

    def command(self, command_name):

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"[{datetime.datetime.now().strftime("%H:%M:%S")}]")

                return func(*args, **kwargs)

            self._BOT_COMMANDS[command_name] = wrapper
            print(f"COMMAND IS REGISTERED /{command_name}")
            return wrapper

        return decorator

    def is_command(self, message):
        return message.startswith("/")

    def process_message(self, message):
        if self.is_command(message):
            command = message.split(" ")[0][1:]
            message_text = " ".join(message.split(" ")[1: ])
            if command in self._BOT_COMMANDS:
                print(f"Command processing [{command}")
                return self._BOT_COMMANDS[command](message_text)
            else:
                print(f"Not cached command {command}")
                return "Command not defined"
        else:
            print("Its not a command")
            return message

bot = TelegramBot()
@bot.command("start")
def handle_start(message):
    return "Hello^ it is messagee from start"

@bot.command()
def handle_help(message):
    return "Commands: /help, /start"



bot.process_message("/help Help me")
bot.process_message("/start Init message")
bot.process_message("Some message from bot")

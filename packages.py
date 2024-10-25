my_package/
    __init__.py
    greetings.py
    farewells.py
    utils.py
main.py

# my_package/__init__.py
#Actual program starts

from .greetings import greet_morning, greet_evening
from .farewells import say_goodbye
from .utils import get_current_time

print("my_package loaded successfully!")
# my_package/greetings.py

def greet_morning():
    return "Good morning! Have a great day ahead!"

def greet_evening():
    return "Good evening! Hope you had a wonderful day!"
# my_package/farewells.py

def say_goodbye():
    return "Goodbye! See you soon!"
# my_package/utils.py
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")
# main.py

import my_package

# Greet based on time
current_time = my_package.get_current_time()
print(f"Current Time: {current_time}")

hour = int(current_time[:2])
if hour < 12:
    print(my_package.greet_morning())
else:
    print(my_package.greet_evening())

# Say goodbye
print(my_package.say_goodbye())

#output example
my_package loaded successfully!
Current Time: 10:30:15
Good morning! Have a great day ahead!
Goodbye! See you soon!
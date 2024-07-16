#imported datetime to access the current year
import datetime

#variable containing the name entered in the input
user_name = input("What is your name? ")
#age string entered from the input being converted to an int type
user_age = int(input("How old are you? "))

#printing the users name, then subtracting the age from the current year
print(f"Hello {user_name}! You were born in { int((datetime.datetime.now().year)) - user_age}.")
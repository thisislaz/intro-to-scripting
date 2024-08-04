input_month = input()
input_day = int(input())

spring = ["March","April","May","June"]
summer = ["June","July","August","September"]
Autumn = ["September",'October','November','December']
winter = ['December','January','February','March']

days_in_month = {
    "January": 31,
    "February": 28,  # Leap year handling can be added if needed
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

if input_day <= 0 or input_month not in days_in_month or input_day > days_in_month[input_month]:
    print("Invalid")
elif (input_month not in spring and
      input_month not in summer and
      input_month not in Autumn and
      input_month not in winter):
    print("Invalid")
elif input_month in spring:
    if input_month == "March" and input_day > 19:
        print("Spring")
    elif input_month == "March" and (input_day == 0 or input_day <= 19):
        print("Winter")
    elif input_month == "June" and input_day < 21:
        print("Spring")
    elif input_month == "June" and input_day == 21:
        print("Summer")
    else:
        print("Spring")
elif input_month in summer:
    if input_month == "June" and input_day > 20:
        print("Summer")
    elif input_month == "September" and input_day < 22:
        print("Summer")
    else:
        print("Summer")
elif input_month in Autumn:
    if input_month == "September" and input_day > 21:
        print("Autumn")
    elif input_month == "December" and input_day < 21:
        print("Autumn")
    else:
        print("Autumn")
elif input_month in winter:
    if input_month == "December" and input_day > 21:
        print("Winter")
    elif input_month == "March" and input_day < 20:
        print("Winter")
    else:
        print("Winter")

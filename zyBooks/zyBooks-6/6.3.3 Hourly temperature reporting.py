user_input = input()
hourly_temperature = user_input.split()

''' Your solution goes here '''
for x in hourly_temperature:
    if x != hourly_temperature[-1]:
        print(x,end=" - > ")
    else:
        print(x)
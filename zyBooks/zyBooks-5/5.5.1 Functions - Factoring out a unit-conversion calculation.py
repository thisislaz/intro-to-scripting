''' Your solution goes here '''

def mph_and_minutes_to_miles(miles,minutes):
    hours_traveled = minutes / 60.0
    miles_traveled = hours_traveled * miles
    return  miles_traveled

miles_per_hour = float(input())
minutes_traveled = float(input())

print('Miles: {:f}'.format(mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)))
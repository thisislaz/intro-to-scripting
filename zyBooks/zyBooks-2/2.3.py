caffeine_content_mg = {
    'Mr. Goodbar chocolate': 122,
    'Red Bull': 33,
    'Monster Hitman Sniper energy drink': 270,
    'Lipton Brisk iced tea - lemon flavor': 2,
    'dark chocolate coated coffee beans': 869,
    'Regular drip or percolated coffee': 60,
    'Buzz Bites Chocolate Chews': 1639
}

for k,v in caffeine_content_mg.items():
    print('Key: ',k,"\nValue: ",v,"\n")

print(caffeine_content_mg['Red Bull'],"\n")

students={}
students["john"] = "a"
print(students)
students['jonnhy']="b"
print(students)
del students['john']
print(students,"\n")
print("----------          2.3.1     -----------------\n")
car_makers = {'Acura': 'Japan', 'Fiat': 'Egypt'}

# Add the key Tesla with value USA to car_makers
# Modify the car maker of Fiat to Italy

car_makers['Fiat']='Italy'
car_makers["Tesla"]="USA"

print('Acura made in', car_makers['Acura'])
print('Fiat made in', car_makers['Fiat'])
print('Tesla made in', car_makers['Tesla'])
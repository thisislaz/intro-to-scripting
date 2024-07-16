name= input()

if len(name.split()) == 3:
    firstName = name.split()[0]
    middleName = name.split()[1]
    lastName = name.split()[-1]

    #prints "Doe, P.S."
    print(f"{lastName.capitalize()}, {firstName[0].upper()}.{middleName[0].upper()}.")
else:
    firstName = name.split()[0]
    lastName = name.split()[-1]
    #prints "Clark, J."
    print(f"{lastName.capitalize()}, {firstName[0].upper()}.")
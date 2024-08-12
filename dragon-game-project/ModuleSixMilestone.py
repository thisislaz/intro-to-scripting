#Lazaro Alvarez

rooms = {
        'Start': {'North': 'Bedroom'},
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

current_room = "Start"
print("Welcome to the Dragon Text Adventure Game")
print("Inorder to move you must select from North,South,East,West")
print("--------------------------------------------------")
while True:
    print()
    print(f"Currently, you are in the {current_room} room.")
    possible_paths = rooms[current_room]
    print("Directions:",end=" ")
    for options in possible_paths:
        print(f"{options}",end=" ")

    user_input = input("\nIn which direction would you like to go? (Type 'exit' to quit): ").capitalize()
    print()
    if user_input == 'Exit':
        print("Exited game.")
        break

    if user_input in possible_paths:
        current_room = possible_paths[user_input]
    else:
        print(f"------- Invalid command!\n------- Please choose one of the available directions.")

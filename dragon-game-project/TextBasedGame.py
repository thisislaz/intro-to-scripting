#Lazaro Alvarez

player_name = input("Welcome to Honey-Do Hero!!\nInorder to play, provide a name: ")

#Initializing room variables
rooms = {
    'balcony': {'south': 'living'},
    'bathroom': {'west': 'living', 'north': 'bedroom', 'south': 'closet'},
    'bedroom': {'south': 'bathroom'},
    'closet': {'north': 'bathroom'},
    'dinning': {'east': 'living', 'south': 'kitchen'},
    'kitchen': {'north': 'dinning'},
    'living': {'north': 'balcony', 'east': 'bathroom', 'west': 'dinning'},
    'start': {'north': 'living', 'west': 'kitchen'}
}

#initializing tasks variables
tasks = {
    'balcony': {'task': 'Wife', 'completed': False},
    'bathroom': {'task': 'clean tub', 'completed': False},
    'bedroom': {'task': 'make bed', 'completed': False},
    'closet': {'task': 'fold clothes', 'completed': False},
    'dinning': {'task': 'vacuum floor', 'completed': False},
    'kitchen': {'task': 'clean stove', 'completed': False},
    'living': {'task': 'dust tv', 'completed': False},
    'start': {'task': None, 'completed': False}
}

#initializing the current room to be the 'start' room
current_room = 'start'

#player's completed tasks list
completed_task_list = []


#function that allows player to check what tasks have been done
def check_completed_tasks(arr):
    tasks = ", ".join(arr)
    print(f"So far you have completed these tasks: {tasks}")


#function to show the game's instructions
def show_instructions():
    print(f"\nHello, {player_name}.")
    print("The rules are simple. Complete your wife's six tasks.")
    print(f"Refuse? {'Fail and lose everything!!'.upper()}\n")
    print("You need to travel from room to room completing each of your tasks.\n"
          "Travel directions: north, south, east, west \n"
          "Complete tasks by typing 'complete' followed by the task name. \n"
          "Have fun and good luck!!\n")


#function that displays possible turns that the hero can take
def display_possible_directions(current_room):
    directions_array = ", ".join(rooms[current_room].keys())
    return directions_array


#display task required within this room
def display_task_within_room(current_room):
    return tasks[current_room]['task']


def show_completed_tasks(completed_task_list):
    task_array = ", ".join(completed_task_list)
    if len(task_array) == 0:
        return None
    return task_array


def complete_task(room_task):
    completed_task_list.append(room_task)


def remove_completed_task_in_room(current_room):
    tasks[current_room]['completed'] = True
    completed_task_list.append(tasks[current_room]['task'])


#main function that starts the game
def main(current_room):
    #calling game instructions function
    show_instructions()

    #starting the while loop that is the game itself
    while True:
        #printing the current room
        print(f"You are currently in the {current_room} room.")

        #printing the completed tasks and how many remain
        print(f"Completed tasks: {show_completed_tasks(completed_task_list)}\n"
              f"{6 - len(completed_task_list)} tasks remain.")

        #printing the available directions for this current room
        print(f"Available directions: {display_possible_directions(current_room)}")
        #checking if the task has been completed
        if tasks[current_room]['completed']:
            #if so print this message
            print(f"Task needed to be completed in this room: {None}")
        else:
            #else print this message
            print(f"Task needed to be completed in this room: {display_task_within_room(current_room)}")

        #here we are obtaining the users input
        user_input = input("\nWhich direction would you like to go? (Type 'exit' to exit the game): ").lower()

        #checking if the user wants to exit the game loop
        if user_input == 'exit':
            print("Exited game.")
            break

        #main decision branch
        #checking if the user input an appropriate direction command
        if user_input in rooms[current_room]:
            #if so set the current room to the room in the direction that the user selected
            current_room = rooms[current_room][user_input]
            #this next if else branch checks if the user checks on the wife before completing all the tasks
            if current_room == 'balcony' and len(completed_task_list) != 6:
                print("You did not finish all the tasks!!\n"
                      "Your wife gets very upset and leaves you!!")
                break
            #this is checking if the user reaches the wife after completing all the tasks
            elif current_room == 'balcony' and len(completed_task_list) == 6:
                print("Congratulations!! You finished all tasks and your wife is very happy!\n"
                      "You have won the Honey-Do Hero Game!!")
                break
        #another if statement checking a possible option for the user to input
        elif user_input == f'complete {display_task_within_room(current_room)}':
            remove_completed_task_in_room(current_room)
        #what the program outputs if the user uses an invalid command
        else:
            print("Invalid command. Try again.\n")


#calling the function that runs the game
main(current_room)

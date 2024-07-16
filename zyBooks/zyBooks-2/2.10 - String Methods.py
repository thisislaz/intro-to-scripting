word = 'onomatopoeia'
num_guesses = 10

hidden_word = '-' * len(word)

guess = 1

while guess <= num_guesses and '-' in hidden_word:
    print(hidden_word)
    user_input = input('Enter a character (guess #{}): '.format(guess))

    if len(user_input) == 1:
        # Count the number of times the character occurs in the word
        num_occurrences = word.count(user_input)

        # Replace the appropriate position(s) in hidden_word with the actual character.
        position = -1
        for occurrence in range(num_occurrences):
            position = word.find(user_input, position + 1)  # Find the position of the next occurrence
            hidden_word = hidden_word[:position] + user_input + hidden_word[position + 1:]  # Rebuild the hidden word string
        guess += 1

if not '-' in hidden_word:
    print('Winner!', end=' ')
else:
    print('Loser!', end=' ')

print('The word was {}.'.format(word))

###
print("-------------                  ----------------                 --------------------")
menu_prompt = ('Available commands:\n'
               '  (add) Add passenger\n'
               '  (del) Delete passenger\n'
               '  (print) Print passenger list\n'
               '  (exit) Exit the program\n'
               'Enter command:\n')

destinations = ['PHX', 'AUS', 'LAS']

destination_prompt = ('Available destinations:\n'
                      '(PHX) Phoenix\n'
                      '(AUS) Austin\n'
                      '(LAS) Las Vegas\n'
                      'Enter destination:\n')

passengers = {}

print('Welcome to Mohawk Airlines!\n')
user_input = input(menu_prompt).strip().lower()

while user_input != 'exit':
    if user_input == 'add':
        name = input('Enter passenger name:\n').strip().upper()
        destination = input(destination_prompt).strip().upper()
        if destination not in destinations:
            print('Unknown destination.\n')
        else:
            passengers[name] = destination

    elif user_input == 'del':
        name = input('Enter passenger name:\n').strip().upper()
        if name in passengers:
            del passengers[name]

    elif user_input == 'print':
        for passenger in passengers:
            print('{} --> {}'.format(passenger.title(), passengers[passenger]))
    else:
        print('Unrecognized command.')

    user_input = input('Enter command:\n').strip().lower()

###
george_v = "His Majesty George V, by the Grace of God, " \
           "of the United Kingdom of Great Britain and " \
           "Ireland and of the British Dominions beyond " \
           "the Seas, King, Defender of the Faith, Emperor of India"
gandhi = 'Mohandas Karamchand Gandhi'
john_f_kennedy = 'JFK'

print(len(george_v), 'characters is much too long of a name!')
print(len(gandhi), 'characters is better...')
print(len(john_f_kennedy), 'characters is short enough.')
print(len("santa"))

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alphabet[0], alphabet[1], alphabet[25])

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# user_number = int(input('Enter number to use as index: '))
# print()
#
# print('\nLetter', user_number, 'of the alphabet is', alphabet[user_number])
print("America"[2])

lower_case_letters=alphabet.lower()
print(f"Caps: {alphabet}\nLower: {lower_case_letters}")

# person_name=input("Enter your name: ")
# person_age=int(input("How old are you: "))
# print('In 5 years', person_name, 'will be', person_age + 5)
#

my_city=input()
my_state=input()
current_time = '2020-07-26 02:12:18:'

log_entry=current_time+" "+my_city+" "+my_state
print(log_entry)
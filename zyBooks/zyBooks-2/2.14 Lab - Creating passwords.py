# a = input()
# b = input()
# c = input()
# print("You entered: {0} {1} {2}".format(a,b,c))
#
# first_password = a+"_"+b
# second_password = c+ a + c
# print("First password: {}".format(first_password))
# print("Second password: {}".format(second_password))
#
# print("Number of characters in {}: {}".format(first_password,len(first_password)))
# print("Number of characters in {}: {}".format(second_password,len(second_password)))

# # FIXME (1): Finish reading another word and an integer into variables.
# # Output all the values on a single line
# answers= input("Enter two words and a number: ")
# favorite_color=answers.split()[0]
# favorite_word=answers.split()[1]
# favorite_number=answers.split()[2]
# print("You entered: {0} {1} {2}\n".format(favorite_color,favorite_word,favorite_number))
#
# # FIXME (2): Output two password options
# password1 = favorite_color+"_"+favorite_word
# password2 = favorite_number+favorite_word+favorite_number
# print('First password: {}'.format(password1))
# print('First password: {}'.format(password2))
#
#
# # FIXME (3): Output the length of the two password options
# print("Number of characters in {}: {}".format(password1,len(password1)))
# print("Number of characters in {}: {}".format(password2,len(password2)))

# Step 1: Prompt the user to enter two words and a number
word1 = input()
word2 = input()
number = input()

# Output the entered values on a single line separated by a space
print(f"You entered: {word1} {word2} {number}\n")

# Step 2: Create and output the passwords
first_password = f"{word1}_{word2}"
second_password = f"{number}{word1}{number}"

print(f"First password: {first_password}")
print(f"Second password: {second_password}\n")

# Step 3: Output the length of each password
print(f"Number of characters in {first_password}: {len(first_password)}")
print(f"Number of characters in {second_password}: {len(second_password)}")

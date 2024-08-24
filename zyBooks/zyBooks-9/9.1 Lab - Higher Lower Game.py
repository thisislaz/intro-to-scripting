import random

lower = int(input("What is the lower bound?: "))
upper = int(input("What is the upper bound?: "))


random_number_generated = random.randint(lower,upper)
print(random_number_generated)
while True:
    guess = int(input("What is your guess?: "))
    if guess < random_number_generated:
        print("Nope, too low")
    elif guess > random_number_generated:
        print("Nope, too high")
    elif guess == random_number_generated:
        print("You got it!")
        break
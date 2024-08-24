import random

seedVal = int(input("What seed should be used? "))
random.seed(seedVal)


lower = int(input("What is the lower bound?"))
upper = int(input("What is the upper bound?"))

if lower > upper:
    print("Lower bound must be less than upper bound.")
    lower = int(input("What is the lower bound?"))
    upper = int(input("What is the upper bound?"))

random_number = random.randint(lower,upper)

while True:
    guess = int(input("What is your guess? "))
    if guess < random_number:
        print("Nope, too low.")
    elif guess > random_number:
        print("Nope, too high.")
    elif guess == random_number:
        print("You got it!")
        break
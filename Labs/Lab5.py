#Stefani Vestring Lab 5 Numbers guessing game

import random
number = random.randrange(1, 10)
guess = int(input("Lucy is staring at you and waiting for you to throw the ball. On average, how many minutes does it take before she starts yelling at you? "))

while number!= guess:
    print
    if guess < number:
        print("She's not THAT impatient.")
        guess = int(input("Guess again! "))
    
    elif guess > number:
        print("That's way too long!")
        guess = int(input("Try again! "))
    else:
        break
print("Congrats! Now go throw the ball!")
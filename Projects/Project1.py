import random

print('Welcome to the giveaway winner generator!')

print('You can enter a list of names to be entered into the giveaway. It will then select a winner at random for you. Convenient, huh?')

print('Enter a name into the generator and press the ENTER key once. Press the ENTER key twice to generate a winner.')

#Winner is the array
winner = []
while True:
        entry = input('Enter a name: ')
        winner.append(entry)
        
        if entry == '':
            break
        
if winner:
        print('Congratulations! ' + random.choice(winner) + ' is the winner!')

#I couldn't figure out how to restart the loop.
#playagain = input('If you would like to try again, please type "y"')
#if playagain == 'y':
#   continue

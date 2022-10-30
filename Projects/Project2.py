import random

print('Welcome to the giveaway winner generator!')

print('You can enter a list of names to be entered into the giveaway. It will then select a winner at random for you.')
print('Convenient, huh?')


#print('Enter a name into the generator and press the ENTER key once. Press the ENTER key twice to generate a winner.')

#Winner is the array
winner = []
while True:
        entry = input('Enter a name: ')
        winner.append(entry)
        
        if entry == '':
            winner.pop() #removes the '' that is appended after hitting ENTER
            print(winner)
        
            print('Would you like to add more names, remove some names, or generate the winner?')
            retry = input('Type "a" to add more names, "r" to remove names, "l" to print current entries, or "g" to generate the winner: ')
            #need to add error for user hitting ENTER without input at the retry input section
        
            if retry == 'a':
                  a = input('Enter a name to be added: ')
                  winner.append(a) #need to correct the syntax to add the part in '' so that it will print correctly
                  print(a + ' has been added to the list.')
                
            elif a == '':
                  print(winner)
                  print(retry)
            
            elif retry == 'r':
                    r = input('Enter a name to be removed: ')
                
                    if r in winner:
                        winner.remove(r)
                        print(r + ' has been removed from the list.') #need to correct the syntax to add the part in '' so that it will print correctly
                
                    elif r == '':
                        print(winner)
                        print(retry)
        
            elif retry == 'g':
                print('Congratulations! ' + random.choice(winner) + ' is the winner!')
                again = input('Would you like to try again? Enter "y" to start over or "n" to quit. WARNING: This will delete all entries!: ')
                
                if again == 'y':
                    winner.clear()
                    print(entry)
                if again == 'n':
                    break
                    
                    #add option to start with new array or old array
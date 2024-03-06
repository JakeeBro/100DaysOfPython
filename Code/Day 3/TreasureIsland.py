print('Welcome to Treasure Island! Your mission is to find the Treasure.')
print('You are standing in a Forest.\n')
choice1 = input('Would you like to go left or right? (left | right)\n').lower()

if choice1 == 'left':
    print('\nYou arrive at a Lake. There is an island in the middle of it.\n')
else:
    print('Game Over')
    exit()

choice2 = input('Would you like to wait for a boat or swim across? (wait | swim)\n').lower()

if choice2 == 'wait':
    print('\nYou arrive safely on the island. There is a house with three doors: red, yellow, and blue.\n')
else:
    print('Game Over')
    exit()

choice3 = input('Which would you like to open? (red | yellow | blue)\n').lower()

if choice3 == 'yellow':
    print('\nYou found the treasure!\n')
elif choice3 == 'red':
    print('Game Over')
    exit()
elif choice3 == 'blue':
    print('Game Over')
    exit()
else:
    print('Game Over')
    exit()

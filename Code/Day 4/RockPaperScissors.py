import random


def string_converter(choice_int):
    if choice_int < 0 or choice_int > 2:
        return
    match choice_int:
        case 0:
            return 'Rock'
        case 1:
            return 'Paper'
        case 2:
            return 'Scissors'


while True:
    while True:
        choice = int(input('Rock, Paper, Scissors, shoot! (0 | 1 | 2)\n'))
        other = random.randint(0, 2)

        if choice < 0 or choice > 2:
            print('\nPlease choose a number from 0 to 2\n')
        elif choice == other:
            print('\nDraw! Try again\n')
        else:
            break

    choiceString = string_converter(choice)
    otherString = string_converter(other)

    defeat = False

    if choice < other:
        defeat = True
        if choice == 0 and other == 2:
            defeat = False

    match defeat:
        case False:
            print(f'{choiceString} beats {otherString}, you win!')
        case True:
            print(f'{otherString} beats {choiceString}, you lose!')

    rerun = int(input('\nWould you like to play again? (0 = No | 1 = Yes)\n'))

    if rerun != 1:
        exit()

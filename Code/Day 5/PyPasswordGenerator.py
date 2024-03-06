import random

print('Welcome to the PyPassword Generator!')
letters = int(input('How many letters would you like in your password?\n'))
symbols = int(input('How many symbols would you like in your password?\n'))
numbers = int(input('How many numbers would you like in your password?\n'))

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '`', '~']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

total = letters + symbols + numbers
remaining = [letters, symbols, numbers]

password = ''

while True:
    group = random.randint(0, 2)
    character = ''
    match group:
        case 0:
            if letters > 0:
                character = letters_list[random.randint(0, len(letters_list) - 1)]
                size = random.randint(1,2)
                if size % 2 == 0:
                    character = character.upper()
                letters -= 1
        case 1:
            if symbols > 0:
                character = symbols_list[random.randint(0, len(symbols_list) - 1)]
                symbols -= 1
        case 2:
            if numbers > 0:
                character = numbers_list[random.randint(0, len(numbers_list) - 1)]
                numbers -= 1

    password += character

    if letters == 0 and symbols == 0 and numbers == 0:
        break

print(password)

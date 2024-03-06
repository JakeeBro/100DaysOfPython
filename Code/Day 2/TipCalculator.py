print("Welcome to the Tip Calculator.")
total_bill = float(input('What was the total bill? $'))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12, or 15?')) / 100
people_split = int(input('How many people will be splitting the bill?'))

bill = (total_bill + (total_bill * tip_percentage)) / people_split

print(f'Each person should pay: ${bill:.2f}')

start = int(input('Starting Number: \n'))
end = int(input('Ending Number: \n'))

totalSum = 0

for n in range(start, end + 1):
    if n % 2 == 0:
        totalSum += n

print(f'The Sum of all Even Numbers between {start} and {end} is {totalSum}')
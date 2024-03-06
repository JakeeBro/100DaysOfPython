scores = input().split()
for score in range(0, len(scores)):
    scores[score] = int(scores[score])

highest = 0
for score in scores:
    if score > highest:
        highest = score

print(f'The highest score is: {highest}')

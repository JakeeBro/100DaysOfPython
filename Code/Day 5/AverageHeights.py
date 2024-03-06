heights = input().split()
for n in range(0, len(heights)):
    heights[n] = int(heights[n])

total = 0
for height in heights:
    total += height
print(f'total height = {total}')

num = 0
for height in heights:
    num += 1
print(f'number of heights = {num}')

print(f'average height = {int(total / num)}')

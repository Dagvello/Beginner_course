world = input()
count = 0
while world != 'стоп' and world != 'хватит' and world != 'достаточно':
    count += 1
    world = input()
print(count)
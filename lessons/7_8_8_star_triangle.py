number = int((int(input()) + 1) / 2)
for i in range(1, number + 1):
    for j in range(i):
        print('*', end='')
    print()
for i in range(number, 1, -1):
    for j in range(i, 1, -1):
        print('*', end='')
    print()

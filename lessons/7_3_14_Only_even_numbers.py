count = 0
for i in range(10):
    number = int(input())
    if number % 2 == 0:
        count += 1

if count == 10:

    print('YES')
else:

    print('NO')

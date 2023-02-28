number = int(input())
total = 0
for n in range(1, number + 1):
    total += n * (-1) ** (n + 1)
print(total)

n = int(input())
maximum1 = 0
maximum2 = 0
for i in range(n):
    number = int(input())
    if number > maximum1:
        maximum2 = maximum1
        maximum1 = number
    elif number > maximum2:
        maximum2 = number
print(maximum1)
print(maximum2)




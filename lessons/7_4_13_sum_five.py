num = int(input())
count = 0
while num >= 0 and num <= 5:
    if num == 5:
        count += 1
    num = int(input())
print(count)
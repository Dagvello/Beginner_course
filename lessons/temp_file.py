number = int(input())
digit = number
count = 0
while number > 0:
    num = number % 10
    count += 1
    number = number // 10
print(count)
print(digit // (10**(count-1)))


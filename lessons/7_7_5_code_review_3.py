s = 0
count = 0
for i in range(7):
    n = int(input())
    if n % 2 == 0:
        s += n
        count += 1
if count == 0:
    print(0)
else:
    print(s)
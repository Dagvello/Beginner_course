mx = float('-inf')
s = 0
count = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
        count += 1
        if x > mx:
            mx = x
if count == 0:
    print('NO')
else:
    print(s)
    print(mx)
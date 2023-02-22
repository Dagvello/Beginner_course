m = int(input())
n = int(input())
if n < m:
    for i in range(m, n-1, -1):
        print(i)
else:
    for i in range(m, n+1):
        print(i)

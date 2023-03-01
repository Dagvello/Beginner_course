n = int(input())
fib1 = 0
fib2 = 1
print(fib2, end=' ')
for i in range(2, n+1):
    fib = fib1 + fib2
    print(fib, end=' ')
    fib1, fib2 = fib2, fib

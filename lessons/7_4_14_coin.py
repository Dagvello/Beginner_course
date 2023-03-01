summa = int(input())
coin = 0
while summa >= 25:
    coin += 1
    summa -= 25
while summa >= 10:
    coin += 1
    summa -= 10
while summa >= 5:
    coin += 1
    summa -= 5
while summa >= 1:
    coin += 1
    summa -= 1
print(coin)

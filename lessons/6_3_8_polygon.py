from math import tan, pi

N = int(input())
A = float(input())

S = N * A ** 2 / (4 * tan(pi / N))

print(S)

# 28n+30k+31m=365
for n in range(100):
    for k in range(100):
        for m in range(100):
            if 28 * n + 30 * k + 31 * m == 365:
                print(n, k, m)

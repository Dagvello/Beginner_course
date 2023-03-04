cache = {}


def find_numbers():
    for a in range(1, 150):
        for b in range(a, 150):
            for c in range(b, 150):
                for d in range(c, 150):
                    e = int((a ** 5 + b ** 5 + c ** 5 + d ** 5) ** (1 / 5))
                    if e ** 5 == a ** 5 + b ** 5 + c ** 5 + d ** 5:
                        cache[(a, b, c, d)] = e

    return cache


result = find_numbers()
print(result)

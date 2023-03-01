def only_even_numbers() -> int:
    count = 0
    for i in range(9):
        number = int(input())
        if number % 2 == 0:
            count += 1
        else:
            return print('NO')
        if count == 10:
            return print('YES')



if __name__ == '__main__':
    only_even_numbers()

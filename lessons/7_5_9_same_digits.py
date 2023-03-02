def same_digits(number: int) -> bool:
    sample = number % 10
    while number > 0:
        num = number % 10
        number = number // 10
        if sample == num:
            flag = True
        else:
            flag = False
    return flag


if __name__ == '__main__':
    if same_digits(int(input())):
        print('YES')
    else:
        print('NO')

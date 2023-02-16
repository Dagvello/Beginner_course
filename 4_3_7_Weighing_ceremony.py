def determination_of_the_weight_category_of_a_boxer(weight: int) -> int:
    """Определение весовой категории боксера"""
    if weight < 60:
        print('Легкий вес')
    elif weight < 64:
        print('Первый полусредний вес')
    else:
        print('Полусредний вес')
    return ''


if __name__ == '__main__':
    print(determination_of_the_weight_category_of_a_boxer(int(input())))

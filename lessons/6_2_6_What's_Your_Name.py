def whats_your_name(first_name: str, last_name: str) -> None:
    """ Функция, которая принимает две строки – имя и фамилию пользователя и выводит фразу:
        «Hello [введенное имя] [введенная фамилия]! You just delved into Python»."""
    print(f'Hello {first_name} {last_name}! You just delved into Python')


if __name__ == '__main__':
    try:
        firstname = input("Введите имя: ")
        lastname = input("Введите фамилию: ")
        if not firstname or not lastname:
            raise ValueError("Необходимо ввести и имя, и фамилию.")
        whats_your_name(firstname, lastname)
    except ValueError as e:
        print(f"Ошибка: {e}")


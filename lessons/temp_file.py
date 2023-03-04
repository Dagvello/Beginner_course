s = input()


def hashtagGen(text: str) -> str:
    """
    Склейка тэгов
    :param text: string
    :return: string
    """

    return '#'+''.join(text.split())


print(hashtagGen(s))
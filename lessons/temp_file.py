s = input()


def hashtaggen(text: str) -> str:
    """
    Склейка тэгов
    :param text: string
    :return: string
    """

    return '#' + ''.join(text.split())


print(hashtaggen(s))

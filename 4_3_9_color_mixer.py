colors = {'красный: 1', 'синий: 2', 'желтый: 3'}
mix_color = {'3: фиолетовый', '4: оранжевый', '5: зеленый'}


def mix_color(color_1: str, color_2: str) -> str:
    """Смешение цветов"""
    if color_1 or color_2 not in colors:
        return print('ошибка цвета')
    else:
        return print(mix_color[colors[color_1] + colors[color_2]])


if __name__ == '__main__':
    color_1, color_2 = input(), input()

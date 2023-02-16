colors = {'красный': 1, 'синий': 3, 'желтый': 6}
mix_colors = {2: 'красный', 4: 'фиолетовый', 6: 'синий', 7: 'оранжевый', 9: 'зеленый', 12: 'желтый'}


def mix_color(color_1: str, color_2: str) -> str:
    """Смешение цветов"""

    if color_1 in 'красныйсинийжелтый' and color_2 in 'красныйсинийжелтый':
        return print(mix_colors[colors[color_1] + colors[color_2]])
    else:
        return print('ошибка цвета')


if __name__ == '__main__':
    color_1, color_2 = input(), input()
    mix_color(color_1, color_2)


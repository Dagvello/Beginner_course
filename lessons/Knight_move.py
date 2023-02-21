def examination(move):
    """Проверка правильности входных данных"""
    valid_squares = [f + r for r in '12345678' for f in 'ABCDEFGH']
    if len(move) != 5:
        return False
    if move[:2] not in valid_squares or move[3:] not in valid_squares:
        return False
    if move[2] != '-':
        return False
    return True

def is_valid_knight_move(move):
    """Проверка правильности хода"""
    file_diff = abs(ord(move[0]) - ord(move[3]))
    rank_diff = abs(int(move[1]) - int(move[4]))
    if file_diff == 1 and rank_diff == 2:
        return True
    if file_diff == 2 and rank_diff == 1:
        return True
    return False


if __name__ == '__main__':

    move = input()
    if examination(move):
        if is_valid_knight_move(move):
            print('YES')
        else:
            print('NO')
    else:
        print('ERROR')

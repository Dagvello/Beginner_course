def is_valid_knight_move(move):
    valid_squares = [f + r for r in '12345678' for f in 'abcdefgh']
    move = move.lower()
    if len(move) != 5:
        return False
    if move[:2] not in valid_squares or move[3:] not in valid_squares:
        return False
    if move[2] != '-':
        return False
    file_diff = abs(ord(move[0]) - ord(move[3]))
    rank_diff = abs(int(move[1]) - int(move[4]))
    if file_diff == 1 and rank_diff == 2:
        return True
    if file_diff == 2 and rank_diff == 1:
        return True
    return False


if __name__ == '__main__':
    # Пример использования функции is_valid_knight_move
    move1 = 'C7-D5'
    move2 = 'E2-E4'
    move3 = 'D9-N5'
    print(is_valid_knight_move(move1))  # True
    print(is_valid_knight_move(move2))  # False
    print(is_valid_knight_move(move3))  # False

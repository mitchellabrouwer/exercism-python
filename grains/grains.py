CHESS_BOARD_SQUARES = 64


def square(number):
    if number < 1 or number > CHESS_BOARD_SQUARES:
        raise ValueError("square not valid")

    return 2 ** (number - 1)


def total():
    return square(CHESS_BOARD_SQUARES) * 2 - 1

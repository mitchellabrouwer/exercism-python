from typing import Callable


def leap_year(year: int) -> bool:
    divisible_by: Callable[[int], bool] = lambda x: year % x == 0
    return divisible_by(4) and not divisible_by(100) or divisible_by(400)

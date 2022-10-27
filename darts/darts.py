import math

DISTANCE_FROM_CENTER_SCORE = {1: 10, 5: 5, 10: 1}


def score(x: int, y: int) -> int:
    """Determine the points earned in a single toss of a darts game."""
    distance = math.sqrt(x ** 2 + y ** 2)

    for threshold, score in DISTANCE_FROM_CENTER_SCORE.items():
        if distance <= threshold:
            return score

    return 0

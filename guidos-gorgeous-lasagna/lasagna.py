EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2


def bake_time_remaining(minutes_in_oven):
    """
    :param elapsed_bake_time: int, baking time already elapsed
    :return: int, remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - minutes_in_oven


def preparation_time_in_minutes(number_of_layers):
    """
    :param number_of_layers: int, number of lasagna layers
    :return: int, numbers of layers multiplied by the 'PREPARATION_TIME_PER_LAYER'

    Function that calculates the time to prepare lasagna based on number of layers
    """

    return number_of_layers * PREPARATION_TIME_PER_LAYER


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    :param number_of_layers: int, number of lasagna layers
    :param elapsed_bake_time: int, time the lasagna has already been in the oven
    :return: int, numbers of layers multiplied by the 'PREPARATION_TIME_PER_LAYER'

    Function that sums preparation time and elapsed time when making lasagna
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

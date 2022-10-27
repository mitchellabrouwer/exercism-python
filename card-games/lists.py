from typing import List

JACK = 11


def get_rounds(number: int):
    """

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return list(range(number, number + 3))


def concatenate_rounds(rounds_1: List[int], rounds_2: List[int]):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return [*rounds_1, *rounds_2]


def list_contains_round(rounds: List[int], number: int):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand: List[int]):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand: List[int]):
    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """

    first_and_last = (hand[0] + hand[-1]) / 2
    median = hand[(len(hand) // 2)]
    average = card_average(hand)

    return average in (first_and_last, median)


def average_even_is_average_odd(hand: List[int]):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    return card_average(hand[::2]) == card_average(hand[1::2])


def maybe_double_last(hand: List[int]):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    return [card == JACK and card * 2 or card for card in hand]

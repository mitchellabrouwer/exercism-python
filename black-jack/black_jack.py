"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


from typing import List, Tuple, Union


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """

    if card == "A":
        return 1
    if card in "JQK":
        return 10
    return int(card)


def higher_card(*cards: List[str]) -> Union[Tuple[str, str], str]:
    """Determine which card has a higher value in the hand.

    : param cards: str[] - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    : return: higher value card - str. Tuple of both cards if they are of equal value.
    """

    assert len(cards) == 2

    score = value_of_card(cards[0]), value_of_card(cards[1])

    if score[0] > score[1]:
        return cards[0]
    elif score[1] > score[0]:
        return cards[1]
    return cards


def value_of_ace(*cards: List[str]) -> int:
    """Calculate the most advantageous value for the ace card.

    : param cards: str[] - card dealt. 'J', 'Q', 'K' = 10; 'A' = 11 (if already in hand); numerical value otherwise.
    : return: int - value of the upcoming ace card(either 1 or 11).
    """

    total = sum(value_of_card(c) for c in cards)

    if "A" in cards or total + 11 > 21:
        return 1
    return 11


def is_blackjack(*cards: List[str]) -> int:
    """Determine if the hand is a 'natural' or 'blackjack'.

    : param cards: str[] - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    : return: bool - if the hand is a blackjack(two cards worth 21).
    """

    assert len(cards) == 2

    points = sum(value_of_card(c) for c in cards)

    if "A" in cards:
        points += 10

    return points == 21


def can_split_pairs(*cards: List[str]) -> bool:
    """Determine if a player can split their hand into two hands.

    : param cards: str[] - cards dealt.
    : return: bool - if the hand can be split into two pairs(i.e. cards are of the same value).
    """

    assert len(cards) == 2

    return value_of_card(cards[0]) == value_of_card(cards[1])


def can_double_down(*cards: List[str]) -> bool:
    """Determine if a blackjack player can place a double down bet.

    : param cards: str[] - first and second cards in hand.
    : return: bool - if the hand can be doubled down(i.e. totals 9, 10 or 11 points).
    """

    assert len(cards) == 2

    points = sum(value_of_card(c) for c in cards)

    return 9 <= points <= 11

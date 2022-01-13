"""

"""
from constants import suits


def create(value, suit):
    """
    Given a value and a suit, return a representation of a card
    containing the value and the suit
    :param value: number of the card (1-13)
    :param suit: suit of the card (1-4)
    :return:
    """
    return (value, suit)


def as_str(card):
    """
    Given a card, return a print-ready string
    :param card: the card object with value & suit
    :return: a string -> the prettified version of the card object
    """
    return "[{0}{1}]".format(card[0], suits[card[1] - 1])


if __name__ == "__main__":
    print(create(13, 3))
    print(as_str(create(10, 2)))

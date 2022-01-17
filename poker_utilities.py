"""
Functions for classifying poker hands
Author: Nick DeBaise

Note on refactor:
    One of my functions (is_continuous_hand) contained logic for sorting, storing, and classifying
    a flush. I decided to split that logic up into 3 different funcs, which proved helpful in the future.
    The three new funcs are is_continuous_hand, put_in_dict (deck_utilities) and sort_by_value (deck_utilities)
    These three funcs were useful as I reused them in other classification functions even though I wrote those
    after refactoring. Initially, I had the 3 funcs all in poker_utils but thought that deck_utilities
    would be a better place for put_in_dict and sort_by_value, so I refactored those out of this file.
"""
import card_utilities as card_utils
import deck_utilities as deck_utils


def is_pair(hand):
    """
    Given a standard 5 card poker hand, return whether there is a pair or three of a kind
    :param hand: Standard 5 card poker hand
    :return: True if there is one of those pairs, False if not
    """

    dict = deck_utils.put_in_dict(hand)

    num_pairs = 0
    is_three_kind = False

    for key in dict.keys():
        if dict[key] == 2:
            num_pairs += 1

        if dict[key] == 3:
            is_three_kind = True

    return is_three_kind or num_pairs == 1


def is_two_pair(hand):
    """
    Given a standard 5 card poker hand, return whether there is a 2 pair, 4 of a kind, or full house
    :param hand: Standard 5 card poker hand
    :return: True if there is one of those pairs, False if not
    """

    dict = deck_utils.put_in_dict(hand)

    num_pairs = 0
    is_four_kind = False
    is_three_kind = False

    for key in dict.keys():
        if dict[key] == 2:
            num_pairs += 1

        if dict[key] == 4:
            is_four_kind = True

        if dict[key] == 3:
            is_three_kind = True

    return (is_three_kind and num_pairs == 1) or num_pairs >= 2 or is_four_kind


def classify_flush(hand):
    """
    Given a hand, classify it as a flush or not a flush
    :param hand:
    :return:
    """

    possible_flush = is_continuous_hand(hand)
    if possible_flush is None:
        return False
    return "flush" in possible_flush


def is_continuous_hand(hand):
    """
    Given a standard 5 card poker hand, classify it if there are continuous cards
    :param hand: a standard 5 card poker hand
    :return: "straight" "flush" "royal flush" "straight flush" or None
    """

    # sort the list by value to make it easier
    deck_utils.sort_by_value(hand)

    is_same_suit = True
    possible_flush = True

    suit = card_utils.get_suit(hand[0])
    val = card_utils.get_value(hand[0])

    for i in range(1, len(hand)):
        card = hand[i]
        card_val = card_utils.get_value(card)
        card_suit = card_utils.get_suit(card)

        # check royal flush
        if suit != card_suit:
            is_same_suit = False

        if card_val != val + 1:
            # it's possible it could be royal flush (ace) and ace is seen as value = 1
            if not (card_val == 10 and val == 1):
                possible_flush = False
        val = card_val

    if possible_flush and is_same_suit and card_utils.get_value(hand[4]) == 13:
        return "royal flush"
    elif is_same_suit and possible_flush:
        return "straight flush"
    elif is_same_suit and not possible_flush:
        return "flush"
    elif possible_flush:
        return "straight"
    else:
        return None


if __name__ == "__main__":
    deck = deck_utils.shuffle(deck_utils.get_deck())
    hand = deck_utils.deal_hand(deck)

    print(hand)

    print(classify_flush(hand))
    print(classify_flush([(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]))  # true
    print(classify_flush([(1, 1), (12, 1), (11, 1), (10, 1), (13, 1)]))  # true
    print(classify_flush([(5, 1), (12, 1), (9, 1), (10, 1), (3, 1)]))  # true
    print(classify_flush([(5, 1), (3, 3), (6, 2), (7, 1), (4, 1)]))  # false
    print("----")
    print(is_two_pair(hand))
    print(is_two_pair([(1, 1), (1, 2), (1, 3), (1, 4), (4, 2)]))  # true
    print(is_two_pair([(2, 1), (2, 2), (1, 3), (1, 4), (4, 2)]))  # true
    print(is_two_pair([(1, 1), (4, 2), (1, 3), (5, 4), (9, 2)]))  # false
    print("----")
    print(is_pair(hand))
    print(is_pair([(1, 1), (1, 2), (1, 3), (1, 4), (4, 2)]))  # false
    print(is_pair([(2, 1), (2, 2), (1, 3), (1, 4), (4, 2)]))  # false
    print(is_pair([(1, 1), (4, 2), (1, 3), (5, 4), (9, 2)]))  # true

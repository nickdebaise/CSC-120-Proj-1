"""
Functions for creating, shuffling, dealing, sorting, and printing a deck/hands in a deck
Author: Nick DeBaise

Note on refactor:
    The only functions I refactored were put_in_dict and sort_by_value. I moved these funcs into this file
    as I thought that these two functions only handled behaviour based on a deck/hand of cards (list)
    They were better suited for this file.
"""
import random

import card_utilities as cards


def put_in_dict(hand):
    """
    Given a list of cards (usually a standard 5 card hand), put all items into a dict with the keys as the values of the
    cards and the values being the num of cards in the hand that match that value
    :param hand: poker hand (list of cards)
    :return: dict with keys as card values and values as number of that card in hand
    """

    dict = {}

    for card in hand:
        val = str(cards.get_value(card))

        if val in dict.keys():
            dict[val] += 1
        else:
            dict[val] = 1

    return dict


def sort_by_value(hand):
    """
    Given a hand/deck (list of cards), sort it by increasing value (1 -> 13), disregarding suit
    :param hand: the hand or deck (list) of cards
    :return: nothing
    """

    hand.sort(key=lambda card: cards.get_value(card))


def get_deck():
    """
    Create and return a list of 52 standard playing cards
    :return: a list of cards
    """

    deck = []

    for i in range(1, 5):
        for j in range(1, 14):
            card = cards.create(j, i)
            deck.append(card)
    return deck


def shuffle(deck):
    """
    Given a deck of cards, randomize the order and return it
    :param deck: a list of cards
    :return: the newly randomized list
    """

    for i in range(0, 52):
        ind = random.randint(0, 51)

        el1 = deck.pop(i)
        el2 = deck.pop(ind - 1)

        deck.insert(i, el2)
        deck.insert(ind, el1)
    return deck


def deal(deck):
    """
    Given a deck, deal one card from the top (removes it from the deck) and return the card
    :param deck: the deck (list) of cards
    :return: a card
    """

    return deck.pop(random.randint(0, len(deck) - 1))


def deal_hand(deck, num_of_cards_in_hand=5):
    """
    given a deck and a number of cards, deal the num of cards off the top of the deck and return that new list
    :param deck: the list of cards to be used to deal
    :param num_of_cards_in_hand: the number of cards to deal
    :return: a list of the cards from the top of the deck
    """

    hand = []
    for _ in range(0, num_of_cards_in_hand):
        hand.append(deal(deck))

    return hand


def print_as_str(deck):
    """
    Given a list of cards, return the list in a print-ready string format
    :param deck: the list of cards
    :return: a prettified print-ready string
    """

    return " | ".join([cards.as_str(card) for card in deck])


if __name__ == "__main__":
    deck = get_deck()

    print(shuffle(deck))
    print(print_as_str(deck))

    for i in range(0, 52):
        print(deal(deck))
    print(len(deck))

    deck2 = get_deck()

    print(deal_hand(deck2))

# This is a sample Python script.
"""
do we pop the card off the list and remove it?
"""
import deck_utilities as deck


def run():
    cards = deck.get_deck()
    cards = deck.shuffle(cards)

    num_pairs = 0
    num_2_pairs = 0
    num_flushes = 0
    num_high_cards = 0

    for i in range(0,10000):
        if len(cards) <= 5:
            cards = deck.get_deck()
            cards = deck.shuffle(cards)
        hand = deck.deal_hand(cards)
        print(deck.print_as_str(hand))


if __name__ == '__main__':
    run()

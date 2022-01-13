# This is a sample Python script.
"""
do we pop the card off the list and remove it?
"""
import deck_utilities as deck
import poker_utilities as poker_utils


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

        if poker_utils.classify_flush(hand):
            num_flushes += 1
        elif poker_utils.is_two_pair(hand):
            num_2_pairs += 1
        elif poker_utils.is_pair(hand):
            num_pairs += 1
        else:
            num_high_cards += 1

    print(num_flushes,  num_2_pairs, num_pairs, num_high_cards)


if __name__ == '__main__':
    run()

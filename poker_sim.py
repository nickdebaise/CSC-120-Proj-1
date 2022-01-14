# This is a sample Python script.
"""
do we pop the card off the list and remove it?
"""
import deck_utilities as deck
import display_utilities as display_utils
import poker_utilities as poker_utils


def play_rounds():
    cards = deck.get_deck()
    cards = deck.shuffle(cards)

    display_utils.print_headers()

    for j in range(1, 11):

        num_pairs = 0
        num_2_pairs = 0
        num_flushes = 0
        num_high_cards = 0

        for i in range(0, j * 10000):
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

        display_utils.print_row(display_utils.get_display_data(num_pairs, num_2_pairs, num_flushes, num_high_cards, j * 10000))


if __name__ == '__main__':
    play_rounds()

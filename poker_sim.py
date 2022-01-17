"""
Simulate games of poker to track different statistics on likelihood of hands

Author: Nick DeBaise
Note: I affirm that I have carried out the attached academic endeavors with full academic honesty,
        in accordance with the Union College Honor Code and the course syllabus.
Note on refactor:
    I gave a lot of thought to functions, behavior, and implementation before writing them which
    ensured that I did not have to refactor a significant portion of my code. With that being said,
    some functions required some refactoring due to too much logic in them or poor initial assessment
    of what the function should do. These are noted at the top of each file in a comment.
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

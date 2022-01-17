"""
Functions for printing card data in a table
Author: Nick DeBaise

Note on refactor:
    I attempted to modularize many functions such as preparing the data, printing headers, printing rows
    to ensure that, if in the future, more columns are added, data changes, headers change, etc, it becomes
    easier to make those changes.
    I think I could have modularized the print_row function a bit more by printing the pairs in the row
    (eg. the number of cards paired with the percentage of those cards) to allow for more columns to be added easier
    but, it also could add more complexity right now considering it may not be used in the future.

"""


def get_display_data(num_pairs, num_2_pairs, num_flushes, num_high_cards, number_items):
    """
    Given card data, return a list with 9 items, each containing the appropriate data for the table
    :param num_pairs: the number of pairs/three of a kind in the sequence
    :param num_2_pairs: the number of 2 pairs, four of a kind, & full houses in the sequence
    :param num_flushes: the number of flushes (normal, royal, straight) in the sequence
    :param num_high_cards: the number of high card/straights in the sequence
    :param number_items: the number of times that the poker game was simulated
    :return: list of card data in order with percentages
    """

    return [number_items, num_pairs, num_pairs / number_items * 100, num_2_pairs, num_2_pairs / number_items * 100,
            num_flushes, num_flushes / number_items * 100, num_high_cards, num_high_cards / number_items * 100]


def print_headers():
    """
    Print the header text in a designated format
    """

    print("{:>10}  {:>8}  {:^5}  {:>10}  {:^5}  {:>10}  {:^5}  {:>10}  {:^5}".format(
        "# of hands", "pairs", "%", "2 pairs", "%", "flushes", "%", "high card", "%"
    ))


def print_row(data):
    """
    Given a list of data for the row, print it in a designated format
    :param data: the list (length = 9) of data for cards
    """

    print("{:>10,d}  {:>8}  {:0>5.2f}  {:>10}  {:0>5.2f}  {:>10}  {:0>5.2f}  {:>10}  {:0>5.2f}".format(
        data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]
    ))


if __name__ == "__main__":
    print_headers()
    print_row([10000, 5061, 51.92231, 4800, 47.02, 451, 2.001, 21, 0.04])
    print_row([50000, 5061, 51.92231, 4800, 47.02, 451, 2.001, 21, 0.04])
    print_row([10000, 5061, 51.92231, 4800, 47.02, 451, 2.001, 21, 0.04])
    print_row([10000, 5061, 51.92231, 4800, 47.02, 451, 2.001, 21, 0.04])
    print_row([100000, 5061, 51.92231, 4800, 47.02, 451, 2.001, 21, 0.04])

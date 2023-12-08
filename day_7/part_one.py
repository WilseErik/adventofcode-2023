""" Solution to part one of day 7 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
from enum import IntEnum
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 7
CORRECT_EXAMPLE_ANSWER = 6440

class HandType(IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

CARD_STRENGT_DICT = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9,
                     '8':8,'7':7, '6':6, '5':5, '4':4, '3':3, '2':2}

class Hand:
    """ Holds the hand of cards """

    def __init__(self, line):
        self.cards = line.split()[0]
        self.bid = int(line.split()[1])
        counts = [self.cards.count(card) for card in CARD_STRENGT_DICT]
        self.type = HandType.HIGH_CARD
        if 5 in counts:
            self.type = HandType.FIVE_OF_A_KIND
        elif 4 in counts:
            self.type = HandType.FOUR_OF_A_KIND
        elif 3 in counts and 2 in counts:
            self.type = HandType.FULL_HOUSE
        elif 3 in counts:
            self.type = HandType.THREE_OF_A_KIND
        elif counts.count(2)==2:
            self.type = HandType.TWO_PAIR
        elif 2 in counts:
            self.type = HandType.ONE_PAIR

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        else:
            for a, b in zip(self.cards, other.cards):
                if a != b:
                    return CARD_STRENGT_DICT[a] < CARD_STRENGT_DICT[b]
        return False


def solve(input_lines):
    hands = sorted(Hand(line) for line in input_lines)
    return sum([index*hand.bid for index, hand in enumerate(hands, 1)])

if __name__ == '__main__':
    advent_util.run(
                    'test_input_part_one.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)

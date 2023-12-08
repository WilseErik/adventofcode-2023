""" Solution to part two of day 7 of Advent of code 2023
    See https://adventofcode.com/2023 for the problem description """

import sys
from enum import IntEnum
sys.path.append('../lib')
#pylint: disable=wrong-import-position
import advent_util
#pylint: enable=wrong-import-position

CURRENT_DAY = 7
CORRECT_EXAMPLE_ANSWER = 5905

class HandType(IntEnum):
    ERROR = 9
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

CARD_STRENGT_DICT = {'A':14, 'K':13, 'Q':12, 'J':1, 'T':10, '9':9,
                     '8':8,'7':7, '6':6, '5':5, '4':4, '3':3, '2':2}

# Map how jokers raise the hand type
JOKER_TYPE_MAP = [#__0__1__2__3__4__5__6__ # Type without jokers
                    [0, 1, 2, 3, 4, 5, 6], # 0 jokers
                    [1, 3, 4, 5, 5, 6, 9], # 1 jokers
                    [3, 5, 9, 6, 9, 9, 9], # 2 jokers
                    [5, 6, 9, 9, 9, 9, 9], # 3 jokers
                    [6, 9, 9, 9, 9, 9, 9], # 4 jokers
                    [6, 9, 9, 9, 9, 9, 9], # 5 jokers
                 ]

class Hand:
    """ Holds the hand of cards """

    def __init__(self, line):
        self.cards = line.split()[0]
        self.bid = int(line.split()[1])
        counts = [self.cards.count(card)
                  for card in CARD_STRENGT_DICT if 'J'!=card]
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
        self.type = JOKER_TYPE_MAP[self.cards.count('J')][self.type]
        assert self.type != HandType.ERROR

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
                    'test_input_part_two.txt',
                    solve,
                    CORRECT_EXAMPLE_ANSWER,
                    CURRENT_DAY)

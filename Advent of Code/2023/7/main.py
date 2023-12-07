from math import sqrt
from typing import Optional
from collections import Counter

INPUT = "input.txt"
DEBUG = False

# INPUT = "sample.txt"
DEBUG = True


def get_hand_rank(hand: str | list[str]) -> int:
    counts = Counter(hand)
    match len(counts):
        case 1:
            return 0
        case 2:
            count = next(iter(counts.values()))
            if count in (1, 4):
                return 1
            return 2
        case 3:
            if any(v == 3 for v in counts.values()):
                return 3
            return 4
        case 4:
            return 5

    return 6


card_ranks = {
    'A': 'a',
    'K': 'b',
    'Q': 'c',
    'J': 'd',
    'T': 'e',
    '9': 'f',
    '8': 'g',
    '7': 'h',
    '6': 'i',
    '5': 'j',
    '4': 'k',
    '3': 'l',
    '2': 'm'
}


def get_sort_key(hand: str) -> tuple[int, str]:  # tuple[type, cards]
    return get_hand_rank(hand), "".join(card_ranks[c] for c in hand)


def p1() -> None:
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    cards_and_bids = [((t := line.split(' '))[0], int(t[1])) for line in lines]

    sort_key_and_bids = sorted([(get_sort_key(t[0]), t[1])
                               for t in cards_and_bids], reverse=True)

    if DEBUG:
        print(cards_and_bids)
        print(sort_key_and_bids)

    ans = 0
    for rank, (_, bids) in enumerate(sort_key_and_bids, start=1):
        ans += rank * bids

    print(ans)


def get_hand_rank2(hand: str) -> int:
    counts = Counter(hand)

    if 'J' not in counts:
        return get_hand_rank(hand)

    return get_hand_rank2_helper([c for c in hand if c != 'J'])


def get_hand_rank2_helper(cards: list[str]) -> int:
    if len(cards) == 5:
        return get_hand_rank(cards)

    best = 10  # no hand rank above this

    for card_replacement in card_ranks2:
        cards.append(card_replacement)
        best = min(best, get_hand_rank2_helper(cards))
        cards.pop()

    return best


card_ranks2 = {
    'A': 'a',
    'K': 'b',
    'Q': 'c',
    'T': 'e',
    '9': 'f',
    '8': 'g',
    '7': 'h',
    '6': 'i',
    '5': 'j',
    '4': 'k',
    '3': 'l',
    '2': 'm',
    'J': 'n',
}


def get_sort_key2(hand: str) -> tuple[int, str]:
    return get_hand_rank2(hand), "".join(card_ranks2[c] for c in hand)


def p2() -> None:
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    cards_and_bids = [((t := line.split(' '))[0], int(t[1])) for line in lines]

    sort_key_and_bids = sorted([(get_sort_key2(t[0]), t[1])
                               for t in cards_and_bids], reverse=True)

    if DEBUG:
        print(cards_and_bids)
        print(sort_key_and_bids)

    ans = 0
    for rank, (_, bids) in enumerate(sort_key_and_bids, start=1):
        ans += rank * bids

    print(ans)


p2()

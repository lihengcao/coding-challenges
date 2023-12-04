# some functions
from enum import IntEnum


def str_find_int(s: str, begin: int, end: int) -> int:
    stop = begin + 1
    while stop < end and s[stop] != ',' and s[stop] != ']':
        stop += 1

    return stop


def str_find_nested_list(s: str, begin: int, end: int) -> int:
    stop = begin + 1
    opens = 1
    while stop < end and not (opens == 1 and s[stop] == ']'):
        if s[stop] == '[':
            opens += 1
        elif s[stop] == ']':
            opens -= 1

        stop += 1

    return stop


def deserialize_nested_list(
        line: str, begin: int = 1, end: int | None = None) -> list:
    if end is None:
        end = len(line) - 1

    deserialized_list = []

    ind = begin
    while ind < end:
        if line[ind] == '[':
            stop = str_find_nested_list(line, ind, end)
            deserialized_list.append(
                deserialize_nested_list(line, ind + 1, stop)
                )
            ind = stop + 2
        else:
            stop = str_find_int(line, ind, end)
            deserialized_list.append(int(line[ind:stop]))
            ind = stop + 1

    return deserialized_list


class ComparisonEnum(IntEnum):
    RIGHT = -1
    INCONCLUSIVE = 0
    WRONG = 1


def compare_packets(l1: list, l2: list) -> ComparisonEnum:
    """
    -1 means right order, l1 is smaller than l2
    0 means inconclusive
    1 means wrong order, l1 is not smaller than l2
    """
    i1, i2 = 0, 0

    while i1 < len(l1) and i2 < len(l2):
        t1, t2 = type(l1[i1]), type(l2[i2])

        if t1 is int is t2:
            if l1[i1] < l2[i2]:
                return ComparisonEnum.RIGHT
            elif l1[i1] > l2[i2]:
                return ComparisonEnum.WRONG

        elif t1 is list is t2:
            recursive_result = compare_packets(l1[i2], l2[i2])
            if recursive_result != ComparisonEnum.INCONCLUSIVE:
                return recursive_result

        else:
            left, right = l1[i1], l2[i2]

            if t1 is int:
                left = [left]
            elif t2 is int:
                right = [right]

            recursive_result = compare_packets(left, right)
            if recursive_result != ComparisonEnum.INCONCLUSIVE:
                return recursive_result

        i1 += 1
        i2 += 1

    if len(l1) == len(l2):
        return ComparisonEnum.INCONCLUSIVE
    elif len(l1) < len(l2):
        return ComparisonEnum.RIGHT
    else:
        return ComparisonEnum.WRONG

# sorting packets

from my_functions import deserialize_nested_list, compare_packets, ComparisonEnum
# from ast import literal_eval
from functools import cmp_to_key


filename = "input.txt"
# filename = "sample.txt"


with open(filename, "r") as f:
    # ast.literal_eval() is cheating... but I did use it to verify correctness
    # packets = [deserialize_nested_list(l.strip()) == literal_eval(l.strip()) for l in f.readlines() if l != '\n']
    # print(all(packets))

    packets = [deserialize_nested_list(line.strip())
               for line in f.readlines() if line != '\n']


def first() -> int:
    return sum(i//2 + 1 for i in range(0, len(packets), 2) if compare_packets(packets[i], packets[i + 1]) is ComparisonEnum.RIGHT)


def second() -> int:
    organized = sorted(packets + [[[2]], [[6]]], key=cmp_to_key(compare_packets))
    d1, d2 = organized.index([[2]]) + 1, organized.index([[6]]) + 1
    return d1 * d2


if __name__ == '__main__':
    print(first())
    print(second())

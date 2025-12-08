from collections import defaultdict


def main():
    rules = defaultdict(set)

    processing_rules = True

    correct_pages_sum = 0

    while True:
        try:
            line = input()
            if line == "":
                processing_rules = False
                continue

            if processing_rules:
                # maybe construct a graph later?
                before, after = tuple(int(n) for n in line.split("|") if n != "")
                rules[before].add(after)
                continue

            update = [int(n) for n in line.split(",") if n != ""]

            if verify_update(rules, update):
                correct_pages_sum += update[len(update) // 2]

        except EOFError:
            break

    print(correct_pages_sum)


def verify_update(rules: dict[int, set[int]], update: list[int]) -> bool:
    for first_i in range(len(update) - 1):
        for second_i in range(first_i + 1, len(update)):
            first, second = update[first_i], update[second_i]
            if first in rules[second]:
                return False

    return True


if __name__ == "__main__":
    main()

from collections import defaultdict


def main():
    left, right = defaultdict(int), defaultdict(int)
    while True:
        try:
            line = input()
            le, ri = [int(n) for n in line.split(" ") if n != ""]

            left[le] += 1
            right[ri] += 1
        except EOFError:
            break

    print(sum(le * right[le] * occur for le, occur in left.items()))


if __name__ == "__main__":
    main()

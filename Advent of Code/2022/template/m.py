# 


filename = "input.txt"
# filename = "sample.txt"


with open(filename, "r") as f:
    arr = [line.strip() for line in f.readlines()]


def first() -> int:
    return 0


def second() -> int:
    return 0


if __name__ == '__main__':
    print("first", first())
    # print("second", second())

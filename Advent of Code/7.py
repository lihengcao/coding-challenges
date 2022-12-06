day = 6
filename = f"{day}.txt"
# filename = f"{day}s.txt"


def first() -> int:
    with open(filename, "r") as f:
        for l in f.readlines():
            pass
    
    return -1

def second():
    pass


if __name__ == '__main__':
    print(first())
    print(second())

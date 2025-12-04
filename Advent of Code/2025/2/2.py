def main():
    ranges: list[tuple[int, int]] = []

    for a in input().split(','):
        x, y = a.split('-')
        ranges.append((int(x), int(y)))
    ranges.sort()

    # print(ranges)

    count = 0

    for a, b in ranges:
        for c in range(a, b + 1):
            if check(c):
                count += c


    print(count)

def check(c: int) -> bool:
    s = str(c)
    
    for mul in range(1, len(s)//2 + 1):
        if len(s) % mul != 0:
            continue

        for j in range(len(s)):
            if s[j] != s[j % mul]:
                break
        else:
            return True
        
    return False


if __name__ == "__main__":
    main()
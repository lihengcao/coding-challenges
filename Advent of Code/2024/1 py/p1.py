def main():
    left, right = [], []

    while True:
        try:
            line = input()
            le, ri = [int(n) for n in line.split(' ') if n != '']
            left.append(le)
            right.append(ri)
        except EOFError:
            break

    left.sort()
    right.sort()

    print(sum(abs(le - ri) for le, ri in zip(left, right)))

if __name__ == "__main__":
    main()
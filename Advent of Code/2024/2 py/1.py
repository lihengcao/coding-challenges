def main():
    safe_reports = 0
    while True:
        try:
            line = [int(n) for n in input().split(' ')]

            safe_reports += int(is_safe(line))

        except EOFError:
            break

    print(safe_reports)

def is_safe(report: list[int]) -> bool:
    increasing = report[0] < report[1]

    for i in range(len(report) - 1):
        d = report[i + 1] - report[i]

        if (d > 0) != increasing or not (1 <= abs(d) <= 3):
            return False

    return True


if __name__ == "__main__":
    main()
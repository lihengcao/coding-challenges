def main():
    safe_reports = 0
    while True:
        try:
            line = [int(n) for n in input().split(' ')]

            safe_reports += int(is_safe(line))
            print(line, safe_reports, end='\n\n')

        except EOFError:
            break

    print(safe_reports)

def is_safe(report: list[int], can_remove=True) -> bool:
    increasing = report[0] < report[1]

    for i in range(len(report) - 1):
        d = report[i + 1] - report[i]

        if (d > 0) != increasing or not (1 <= abs(d) <= 3):
            if not can_remove:
                return False

            # optimizable. lazy. computation cheap enough.
            for di in (-1, 0, 1):
                if not (0 <= i + di < len(report)):
                    continue
                new_input = report[:i + di] + report[i + di + 1:]
                print(new_input)
                if is_safe(new_input, can_remove=False):
                    return True
            return False

    return True


if __name__ == "__main__":
    main()
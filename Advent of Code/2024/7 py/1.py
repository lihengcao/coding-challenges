def main():
    sum_test_values = 0
    while True:
        try:
            line = input()
            raw_target, raw_nums = line.split(":")

            target = int(raw_target)
            nums = [int(n) for n in raw_nums.split(" ") if n != ""]

            if asdf(target, nums):
                sum_test_values += target

        except EOFError:
            break

    print(sum_test_values)


def asdf(target: int, nums: list[int], ind: int = 0) -> bool:
    def h(acc: int, ind: int) -> bool:
        if acc == target:
            return True

        if ind >= len(nums):
            return False

        return h(acc + nums[ind], ind + 1) or h(acc * nums[ind], ind + 1)

    return h(nums[0], 1)


if __name__ == "__main__":
    main()

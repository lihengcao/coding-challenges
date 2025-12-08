def main():
    nums: list[int] = []
    operations: list[str] = []

    while True:
        try:
            inp = input()

            if inp[0] in "+*":
                operations = [e for e in inp.split(" ") if e != ""]
                continue

            if not nums:
                nums = [0] * len(inp)
            for i, n in enumerate(inp):
                if n == " ":
                    continue

                nums[i] = 10 * nums[i] + int(n)
        except EOFError:
            break

    # print(nums)
    # print(operations)

    total = 0
    op_ind = 0
    n_ind = 0
    running = 0

    while op_ind < len(operations):
        if operations[op_ind] == "+":
            running = 0
        else:
            running = 1

        while n_ind < len(nums) and (n := nums[n_ind]) != 0:
            if operations[op_ind] == "+":
                running += n
            else:
                running *= n

            n_ind += 1

        total += running
        op_ind += 1
        n_ind += 1

    print(total)


if __name__ == "__main__":
    main()

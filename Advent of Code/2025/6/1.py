def main():
    nums: list[list[int]] = []
    operations: list[str] = []

    while True:
        try:
            i = input()

            if i[0] in "+*":
                operations = [e for e in i.split(" ") if e != ""]
            else:
                nums.append([int(e) for e in i.split(" ") if e != ""])
        except EOFError:
            break

    total = 0

    for c in range(len(nums[0])):
        if operations[c] == "*":
            a = 1
            for i in range(len(nums)):
                a *= nums[i][c]
        else:
            a = 0
            for i in range(len(nums)):
                a += nums[i][c]
        total += a

    print(total)


if __name__ == "__main__":
    main()

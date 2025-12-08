def read_input():
    return input()


def main():
    file = read_input()

    print(calc_final_checksum(file))


# hey... it fits in memory
def calc_final_checksum(file: str) -> int:
    expanded_disk = []

    for i in range(len(file)):
        if i % 2 == 0:
            expanded_disk.extend([i // 2] * int(file[i]))
        else:
            expanded_disk.extend([None] * int(file[i]))

    print(expanded_disk)

    left, right = 0, len(expanded_disk) - 1

    while left < right:
        if expanded_disk[left] is not None:
            left += 1
        elif expanded_disk[right] is None:
            right -= 1
        else:
            expanded_disk[left] = expanded_disk[right]
            expanded_disk[right] = None
            left += 1
            right -= 1

    print(expanded_disk)

    count = 0
    for ind, id in enumerate(expanded_disk):
        if id is None:
            return count

        count += ind * id

    return count


if __name__ == "__main__":
    main()

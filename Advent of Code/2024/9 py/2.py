def read_input():
    return input()


def main():
    file = read_input()

    print(calc_final_checksum(file))


# hey... it fits in memory
def calc_final_checksum(compressed_file: str) -> int:
    expanded_disk = []
    free_space = []
    files = []

    for i in range(len(compressed_file)):
        val = int(compressed_file[i])
        if i % 2 == 0:
            files.append([len(expanded_disk), val])
            expanded_disk.extend([i // 2] * val)
        else:
            free_space.append([len(expanded_disk), val])
            expanded_disk.extend([None] * val)

    print("free", free_space)
    print("files", files)
    print("disk", expanded_disk)

    for files_ind in range(len(files) - 1, -1, -1):
        move_to_free_ind = None
        file_loc, file_size = files[files_ind]
        for free_space_ind in range(len(free_space)):
            free_loc, free_space_size = free_space[free_space_ind]

            # potentiali bsearch opti
            if file_loc < free_loc:
                continue

            if free_space_size >= file_size:
                # in theory files_ind should still be accesible after the break, but let me be clear!
                move_to_free_ind = free_space_ind
                break

        if move_to_free_ind is not None:
            move(expanded_disk, free_space, files, move_to_free_ind, files_ind)

    print("disk", expanded_disk)

    count = 0
    for ind, id in enumerate(expanded_disk):
        if id is None:
            continue

        count += ind * id

    return count


def move(
    expanded_disk: list[int], free_space, files, free_space_ind, files_ind
) -> None:
    file_loc, file_size = files[files_ind]
    free_loc, free_space_size = free_space[free_space_ind]
    for i in range(file_size):
        expanded_disk[free_loc + i] = files_ind
        expanded_disk[file_loc + i] = None

    free_space[free_space_ind][1] -= file_size

    # might not be an optimization
    # if free_space[free_space_ind][1] == 0:
    #     free_space.pop(free_space_ind)
    # else:

    free_space[free_space_ind][0] += file_size


if __name__ == "__main__":
    main()

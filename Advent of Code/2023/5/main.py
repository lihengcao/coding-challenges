# from math import inf
from typing import Optional

INPUT = "input.txt"
DEBUG = False

# INPUT = "sample.txt"
# DEBUG = True


def find_range(
    map_: list[tuple[int, int, int]], num: int
) -> Optional[tuple[int, int, int]]:
    # small enough that linear search is fine ...

    for i in range(len(map_) - 1, -1, -1):
        range_ = map_[i]

        if range_[1] <= num < range_[1] + range_[2]:
            return range_

    return None


def conv_seed_to_location(maps: list[list[tuple[int, int, int]]], seed: int) -> int:
    cur = seed
    for map_ in maps:
        if DEBUG:
            print(cur)

        maybe_range = find_range(map_, cur)
        if maybe_range is None:
            continue

        cur += maybe_range[0] - maybe_range[1]

    return cur


def p1() -> None:
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

        seeds = [int(e) for e in lines[0].split(":")[1].split(" ") if e != ""]
        maps: list[list[tuple[int, int, int]]] = [[]]

        i_line = 3

        while i_line < len(lines):
            line = lines[i_line]
            if line == "":
                maps[-1].sort(key=lambda t: t[1])
                maps.append([])
                i_line += 2
                continue

            tup = tuple(int(e) for e in line.split(" ") if e != "")
            assert len(tup) == 3
            maps[-1].append(tup)

            i_line += 1

    if DEBUG:
        print(seeds)
        [print(map_) for map_ in maps]

        print([conv_seed_to_location(maps, s) for s in seeds])

    print(min(conv_seed_to_location(maps, s) for s in seeds))


def p2() -> None:
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

        seeds_raw = [int(e) for e in lines[0].split(":")[1].split(" ") if e != ""]
        seeds = [(seeds_raw[i], seeds_raw[i + 1]) for i in range(0, len(seeds_raw), 2)]
        maps: list[list[tuple[int, int, int]]] = [[]]

        i_line = 3

        while i_line < len(lines):
            line = lines[i_line]
            if line == "":
                maps[-1].sort(key=lambda t: t[1])
                maps.append([])
                i_line += 2
                continue

            tup = tuple(int(e) for e in line.split(" ") if e != "")
            assert len(tup) == 3
            maps[-1].append(tup)

            i_line += 1

    if DEBUG:
        print(seeds)
        [print(map_) for map_ in maps]
        print()

    current_ranges = seeds

    for map_ in maps:
        new: list[tuple[int, int]] = []

        if DEBUG:
            print(current_ranges, map_)

        for start, c_len in current_ranges:
            end = start + c_len

            while start < end:
                range_ = find_range(map_, start)
                if DEBUG:
                    print(f"found range:{start, end} {range_}")
                if range_ is None:
                    new.append((start, end - start))
                    break

                d_start, s_start, r_len = range_
                s_end = s_start + r_len

                # i think the first two conditions might be guaranteed
                if s_start <= start < end <= s_end:
                    new.append((start - s_start + d_start, end - start))
                    break

                assert s_start <= start < s_end <= end
                new_range_len = s_end - start
                new.append((start - s_start + d_start, new_range_len))

                start = s_end

        current_ranges = new

    print(min(r[0] for r in current_ranges))


p2()

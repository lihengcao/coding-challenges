from typing import Optional
from functools import reduce

def main():
    banks: list[list[int]] = []

    while True:
        try:
            line = input()
            line = list(line)
            banks.append([int(e) for e in line])
        except EOFError:
            break

    total = 0
    for bank in banks:
        # --- Attempt 1
        # decreasing: list[tuple[int, int]] = []

        # for i, n in enumerate(bank):
        #     if not decreasing:
        #         decreasing.append((n, i))
        #         continue
            
        #     while decreasing and decreasing[-1][0] < n:
        #         decreasing.pop()
        #     decreasing.append((n, i))   
        # print("".join([str(t[0]) for t in decreasing]))

        # --- Attempt 2
        # on = [False] * len(bank)
        # on_size = 0
        # mapping: defaultdict[int, list[int]] = defaultdict(list)
        # for i, n in enumerate(bank):
        #     mapping[n].append(i)
            
        # # print(mapping)

        # for n in range(9, 0, -1):
        #     inds = mapping[n]

        #     # print(n, inds)
        #     for i in reversed(inds):
        #         on[i] = True
        #         on_size += 1
        #         if on_size >= 12:
        #             break
        #     else:
        #         continue
        #     break
        
        # j = int("".join([str(bank[i]) for i in range(len(bank)) if on[i]]))
        # print(on, j)
        # print('---')
        # total += j
        
        # --- Attempt 3 ... finally ...
        best: list[int] = []

        start = 0
        for reserved in range(11, -1, -1):
            max_, ind = max_and_ind(bank, start, len(bank) - reserved)

            best.append(max_)
            start = ind + 1

        j = reduce(lambda a, b: a * 10 + b, best)
        print(j)
        print('---')
        total += j

    print(total)

def max_and_ind(arr: list[int], start: Optional[int]=None, stop: Optional[int]=None) -> tuple[int, int]:
    if start is None:
        start = 0
    if stop is None:
        stop = len(arr)

    max_ = arr[start]
    ind = start

    for i in range(start + 1, stop):
        if arr[i] > max_:
            max_ = arr[i]
            ind = i

    return max_, ind


if __name__ == "__main__":
    main()

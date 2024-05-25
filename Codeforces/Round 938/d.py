from collections import Counter

for _ in range(int(input())):
    n, m, k = [int(e) for e in input().split(" ")]

    a = [int(e) for e in input().split(" ")]
    b = [int(e) for e in input().split(" ")]
    c = a[:m]

    # print(c)

    target_counter = Counter(b)
    current_counter = Counter()

    overlap = 0

    for v in c:
        if v not in target_counter:
            continue

        if v not in current_counter:
            current_counter[v] = 1
            overlap += 1
        elif current_counter[v] < target_counter[v]:
            overlap += 1
            current_counter[v] += 1
        else:
            current_counter[v] += 1

    good_subs = 1 if overlap >= k else 0

    for i in range(n - m):
        remove = a[i]
        add = a[i + m]

        if add != remove:
            if remove in target_counter:
                current_counter[remove] -= 1

                if current_counter[remove] < target_counter[add]:
                    overlap -= 1

            if add in target_counter:
                if add not in current_counter:
                    current_counter[add] = 1
                    overlap += 1
                else:
                    if current_counter[add] < target_counter[add]:
                        overlap += 1

                    current_counter[add] += 1

        good_subs += 1 if overlap >= k else 0

        # print(remove, add, overlap, current_counter)

    print("---")
    print(good_subs)

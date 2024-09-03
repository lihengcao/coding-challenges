from collections import Counter

for _ in range(int(input())):
    n, c, d = [int(e) for e in input().split(" ")]

    arr = sorted([int(e) for e in input().split(" ")])
    arr = Counter(arr)

    done = False
    base_expected = min(arr)

    for _row in range(n):
        expected = base_expected
        for _col in range(n):
            if expected not in arr:
                print("NO")
                done = True
                break

            if arr[expected] == 1:
                del arr[expected]
            else:
                arr[expected] -= 1
            expected += d
        if done:
            break
        base_expected += c
    else:
        print("YES")

"""Round 944 Problem A"""

for _ in range(int(input())):
    a, b = [int(e) for e in input().split(" ")]

    if a > b:
        a, b = b, a

    print(f"{a} {b}")

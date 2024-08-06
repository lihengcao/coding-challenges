from collections import Counter

for _ in range(int(input())):
    n, q = map(int, input().split(' '))
    
    a = input()
    b = input()

    for _ in range(q):
        left, right = map(int, input().split(' '))
        missing = 0

        c = Counter(a[left-1:right])

        for i in range(left-1, right):
            char = b[i]

            if char in c and c[char] > 0:
                c[char] -= 1
            else:
                missing += 1

        print(missing)

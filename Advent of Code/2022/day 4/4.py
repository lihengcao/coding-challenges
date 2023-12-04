def first():
    r = 0
    with open("4.txt", "r") as f:
        for l in f.readlines():
            a, b = l.split(',')
            a1, a2 = [int(n) for n in a.split('-')]
            b1, b2 = [int(n) for n in b.split('-')]

            r += 1 if \
                (b1 <= a1 <= a2 <= b2) or \
                (a1 <= b1 <= b2 <= a2) \
                else 0
            
    return r


def second():
    r = 0
    with open("4.txt", "r") as f:
        for l in f.readlines():
            a, b = l.split(',')
            a1, a2 = [int(n) for n in a.split('-')]
            b1, b2 = [int(n) for n in b.split('-')]

            r += 1 if \
                (b1 <= a1 <= b2) or \
                (b1 <= a2 <= b2) or \
                (a1 <= b1 <= a2) or \
                (a1 <= b2 <= a2) \
                else 0
            
    return r

print(first())
print(second())

def first():
    r = 0
    with open("3.txt", "r") as f:
        for l in f.readlines():
            n = len(l)//2
            l1, l2 = set(l[:n]), l[n:]

            for c in l2:
                if c in l1:
                    r += ord(c) + 1
                    if c.lower() == c:
                        r -= ord('a')
                    else:
                        r -= ord('A') - 26                        
                    break

    return r


def second():
    r = 0
    with open("3.txt", "r") as f:
        ls = [l.strip() for l in f.readlines()]

        for i in range(0, len(ls), 3):
            l1, l2, l3 = ls[i], ls[i + 1], ls[i + 2]

            s = set(l1) & set(l2) & set(l3)

            for c in s:
                r += ord(c) + 1
                if c.lower() == c:
                    r -= ord('a')
                else:
                    r -= ord('A') - 26                        

    return r

print(first())
print(second())

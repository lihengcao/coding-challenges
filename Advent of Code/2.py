my_shape_first = {'X': 1, 'Y': 2, 'Z': 3}


def first():
    score = 0
    with open("2.txt", "r") as f:
        for n in f.readlines():
            t, m = n.strip().split()

            score += my_shape_first[m]

            if ord(t) + 23 == ord(m):
                score += 3
            elif (ord(t) - ord('A') + 1 ) % 3== ord(m) - ord('A') - 23:
                score += 6
                
    return score


my_shape_second = {'X': 0, 'Y': 3, 'Z': 6}


def second():
    score = 0
    with open("2.txt", "r") as f:
        for n in f.readlines():
            t, m = n.strip().split()

            score += my_shape_second[m]

            if m == 'X':
                score += (ord(t) - ord('A') - 1) % 3 + 1
            elif m == 'Y':
                score += (ord(t) - ord('A')) % 3 + 1
            else:
                score += (ord(t) - ord('A') + 1) % 3 + 1
                
    return score



print(first())
print(second())

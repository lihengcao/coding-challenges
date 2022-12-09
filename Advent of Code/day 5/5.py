from typing import List

filename = "5.txt"
# filename = "5s.txt"


# easy way to do this would to hardcode the initial state vs reading the initial state
def get_stacks(arr: List[str]) -> List[List[str]]:
    r_arr, c_arr = len(arr) - 1, (len(arr[-1]) + 1)//4
    stacks = [[None] * r_arr for _ in range(c_arr)]
    
    for r in range(r_arr):
        for i_c in range(c_arr):
            c = arr[r][1 + 4 * i_c]
            if c != ' ':
                stacks[i_c][r_arr - r - 1] = c
                
    return [[e for e in r if e is not None] for r in stacks]
            

def first():
    arr = []
    reading_stacks = True

    with open(filename, "r") as f:
        for l in f.readlines():
            if l == "\n":
                reading_stacks = False
                stacks = get_stacks(arr)
            elif reading_stacks:
                arr.append(l[:-1])
            else:
                l = l.strip().split(' ')
                m, f, t = (int(l[e]) for e in (1, 3, 5,))
                
                for _ in range(m):
                    stacks[t - 1].append(stacks[f - 1].pop())
    
    return ''.join([stacks[i][-1] for i in range(len(stacks))])


def second():
    arr = []
    reading_stacks = True

    with open(filename, "r") as f:
        for l in f.readlines():
            if l == "\n":
                reading_stacks = False
                stacks = get_stacks(arr)
            elif reading_stacks:
                arr.append(l[:-1])
            else:
                l = l.strip().split(' ')
                m, f, t = (int(l[e]) for e in (1, 3, 5,))

                stacks[t - 1].extend(stacks[f - 1][-m:])
                
                for _ in range(m):
                    stacks[f - 1].pop()
    
    return ''.join([stacks[i][-1] for i in range(len(stacks))])


if __name__ == '__main__':
    print(first())    
    print(second())

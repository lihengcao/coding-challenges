from collections import defaultdict


day = 7
filename = f"{day}.txt"
# filename = f"{day}s.txt"


def first() -> int:
    folders = defaultdict(int)
    path = ['/']
    
    with open(filename, "r") as f:
        for l in f.readlines():
            l = l.strip().split(' ')

            if l[0] == "$":
                if l[1] == "cd":
                    if l[2] == "/":
                        path = ['/']
                    elif l[2] == "..":
                        path.pop()
                    else:
                        path.append(l[2])
            elif l[0].isnumeric():
                # print(f"{l[0]=}")
                n = int(l[0])
                p = ""  # folders with the same name but in different directories
                for f in path:
                    p += f
                    folders[p] += n

    # print(folders)
    return sum(n for n in folders.values() if n <= 100_000)

def second() -> int:
    folders = defaultdict(int)
    path = ['/']

    target_free_space = 30000000
    device_total_space = 70000000
    
    with open(filename, "r") as f:
        for l in f.readlines():
            l = l.strip().split(' ')

            if l[0] == "$":
                if l[1] == "cd":
                    if l[2] == "/":
                        path = ['/']
                    elif l[2] == "..":
                        path.pop()
                    else:
                        path.append(l[2])
            elif l[0].isnumeric():
                # print(f"{l[0]=}")
                n = int(l[0])
                p = ""  # folders with the same name but in different directories
                for f in path:
                    p += f
                    folders[p] += n

    current_free_space = device_total_space - folders["/"]
    looking_for = target_free_space - current_free_space
    
    s = folders["/"]
    for k, v in folders.items():
        if looking_for <= v < s:
            s = v

    return s


if __name__ == '__main__':
    print(first())
    print(second())

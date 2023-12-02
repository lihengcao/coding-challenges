INPUT = "i.txt"
DEBUG = False

def day1() -> None:
    R, G, B = 12, 13, 14

    ans = 0
    with open(INPUT, "r") as f:
        lines = f.read().splitlines()

        for line in lines:
            first, second = line.split(':')
            id = int(first.split(' ')[1])

            for set_ in second.split(';'):
                for cube in set_.split(','):
                    cube = cube.lstrip()
                    
                    ending = cube[-1]
                    n = int(cube.split(' ')[0])
                    match ending:
                        case 'd':
                            if n > R:
                                break
                        case 'n':
                            if n > G:
                                break
                        case 'e':
                            if n > B:
                                break
                else:
                    continue
                break
            else:
                ans += id

    print(ans)


def day2() -> None:

    ans = 0
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

        for line in lines:
            _, second = line.split(':')

            r, g, b = 0, 0, 0

            for set_ in second.split(';'):
                for cube in set_.split(','):
                    cube = cube.lstrip()
                    
                    ending = cube[-1]
                    n = int(cube.split(' ')[0])
                    match ending:
                        case 'd':
                            r = max(r, n)
                        case 'n':
                            g = max(g, n)
                        case 'e':
                            b = max(b, n)
            
            ans += r * g * b

    print(ans)

day2()

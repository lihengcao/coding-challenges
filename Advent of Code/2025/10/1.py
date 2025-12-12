from dataclasses import dataclass

@dataclass
class Manual:
    indicator: tuple[int, ...]
    buttons: tuple[tuple[int, ...], ...]

def main():
    manuals = read()    
    
    best = 0
    for m in manuals:
        best += solve(m)

    print(best)


def solve(m: Manual) -> int:
    presses = 0

    q = [tuple([0] * len(m.indicator))]
    tried: set[tuple[int, ...]] = set()

    while q:
        
        new: list[tuple[int, ...]] = []

        for state in q:
            if state == m.indicator:
                return presses
            
            if state in tried:
                continue
            
            tried.add(state)

            for b in m.buttons:
                li = list(state)

                for i in b:
                    li[i] = 1 - li[i]

                t = tuple(li)

                if t not in tried:
                    new.append(t)

        presses += 1
        q = new



    raise ValueError



def read() -> list[Manual]:
    o: list[Manual] = []

    while True:
        try:
            line = input().split(' ')

            s = tuple(1 if c == '#' else 0 for c in line[0][1:-1])

            buttons: list[tuple[int, ...]] = []
            for i in range(1, len(line) - 1):
                buttons.append(tuple(int(e) for e in line[i][1:-1].split(',')))

            o.append(Manual(s, tuple(buttons)))

        except EOFError:
            break

    return o



if __name__ == "__main__":
    main()

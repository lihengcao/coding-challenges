from dataclasses import dataclass

@dataclass
class Manual:
    buttons: tuple[tuple[int, ...], ...]
    joltage: tuple[int, ...]

def main():
    manuals = read()
    
    best = 0
    for m in manuals:
        print(best)
        best += solve(m)

    print(best)


def invalid(target: tuple[int, ...], state: tuple[int, ...]) -> bool:
    for t, s in zip(target, state, strict=True):
        if s > t:
            return True
        
    return False


def solve(m: Manual) -> int:
    presses = 0

    q = [tuple([0] * len(m.joltage))]
    tried: set[tuple[int, ...]] = set()

    while q:
        print(len(q))
        new: list[tuple[int, ...]] = []

        for state in q:
            if state == m.joltage:
                return presses
            
            if invalid(m.joltage, state) or state in tried:
                continue
            
            tried.add(state)

            for b in m.buttons:
                li = list(state)

                for i in b:
                    li[i] += 1
                t = tuple(li)

                if t not in tried and not invalid(m.joltage, t):
                    new.append(t)

        presses += 1
        q = new



    raise ValueError



def read() -> list[Manual]:
    o: list[Manual] = []

    while True:
        try:
            line = input().split(' ')

            buttons: list[tuple[int, ...]] = []
            for i in range(1, len(line) - 1):
                buttons.append(tuple(int(e) for e in line[i][1:-1].split(',')))

            j = tuple(int(e) for e in line[-1][1:-1].split(','))

            o.append(Manual(tuple(buttons), j))

        except EOFError:
            break

    return o



if __name__ == "__main__":
    main()

# monkeys (and number theory)

from typing import Callable


filename = "input.txt"
# filename = "sample.txt"

with open(filename, "r") as f:
    notes = [l.strip() for l in f.readlines()]


class Monkey:
    MOD = 1 << 30
    def __init__(self, index: int, notes: list[str]) -> None:
        self.items: list[int] = [int(n) for n in notes[index + 1].split(': ')[1].split(', ')]
        
        
        operation_line = notes[index + 2].split(' ')[-2:]
        if operation_line[0] == "*":
            if operation_line[1] == "old":
                operation = lambda n: n * n
            else:
                operation = lambda n: n * int(operation_line[1])
        else:
            operation = lambda n: n + int(operation_line[1])
        self.operation: Callable[[int], int] = operation

        self.test_cond_value = int(notes[index + 3].split(' ')[-1])
        test_cond = lambda n: n % self.test_cond_value == 0
        if_true = int(notes[index + 4].split(' ')[-1])
        if_false = int(notes[index + 5].split(' ')[-1])
        self.throw_to: Callable[[int], int] = lambda n: if_true if test_cond(n) else if_false

        self.relief: Callable[[int], int] = lambda n: n//3
    

    def add_item(self, item: int) -> None:
        self.items.append(item)


    def take_turn(self) -> list[list[int]]:
        throws: list[list[int]] = []

        for item in self.items:
            item = self.operation(item)
            item = self.relief(item)
            to = self.throw_to(item)
            throws.append([to, item])

        self.items.clear()

        return throws

    def get_test_cond_value(self) -> int:
        return self.test_cond_value

    def set_relief_func(self, l: Callable[[int], int]) -> None:
        self.relief = l



def first() -> int:
    monkeys: list[Monkey] = []
    
    for i_note in range(0, len(notes), 7):
        monkeys.append(Monkey(i_note, notes))
    
    inspections: list[int] = [0] * len(monkeys)

    for _ in range(20):
        for i_m, m in enumerate(monkeys):
            
            throws = m.take_turn()
            inspections[i_m] += len(throws)

            for to, item in throws:
                monkeys[to].add_item(item)

    inspections.sort()

    return inspections[-1] * inspections[-2]


def second() -> int:
    monkeys: list[Monkey] = []
    
    for i_note in range(0, len(notes), 7):
        monkeys.append(Monkey(i_note, notes))

    mod = 1
    for m in monkeys:
        mod *= m.get_test_cond_value()

    for m in monkeys:
        m.set_relief_func(lambda n: n % mod)
    
    inspections: list[int] = [0] * len(monkeys)

    for i in range(10000):

        for i_m, m in enumerate(monkeys):
            
            throws = m.take_turn()
            inspections[i_m] += len(throws)

            for to, item in throws:
                monkeys[to].add_item(item)

    inspections.sort()

    return inspections[-1] * inspections[-2]


if __name__ == '__main__':
    print(first())
    print(second())

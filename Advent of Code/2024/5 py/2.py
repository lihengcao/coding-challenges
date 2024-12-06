from collections import defaultdict
from typing import Optional

def main():
    rules = defaultdict(set)

    processing_rules = True

    correct_pages_sum = 0

    while True:
        try:
            line = input()
            if line == "":
                processing_rules = False
                # print(rules)
                continue

            if processing_rules:
                # maybe construct a graph later?
                before, after = tuple(int(n) for n in line.split('|') if n != "")
                rules[before].add(after)
                continue

            update = [int(n) for n in line.split(',') if n != ""]

            if verify_update(rules, update):
                continue
            
            update = calc_correct_rev_order(rules, update)
            
            # print(update)

            correct_pages_sum += update[len(update)//2]

        except EOFError:
            break


    print(correct_pages_sum)

def calc_correct_rev_order(rules, update) -> list[int]:
    update = set(update)
    
    def h(candidates: set[int]) -> Optional[list[int]]:
        if not candidates:
            return []
        except_cur = candidates.copy()
        for cur in candidates:
            except_cur.remove(cur)
            if cur in rules and except_cur & rules[cur]:
                except_cur.add(cur)
                continue

            # print("trying ", cur, except_cur)

            res = h(except_cur)
            if res is not None:
                return [cur] + res

            except_cur.add(cur)

        return None


    return h(update)

def verify_update(rules: dict[int, set[int]], update: list[int]) -> bool:
    for first_i in range(len(update) - 1):
        for second_i in range(first_i + 1, len(update)):
            first, second = update[first_i], update[second_i]
            if second not in rules:
                continue
            if first in rules[second]:
                return False

    return True


if __name__ == "__main__":
    main()

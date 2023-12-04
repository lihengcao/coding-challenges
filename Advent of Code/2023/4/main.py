INPUT = "input.txt"
DEBUG = False

# INPUT = "sample.txt"
# DEBUG = True

def p1() -> None:
    ans = 0
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

        for line in lines:
            _, nums = line.split(':')

            winning_nums, my_nums = [[int(n) for n in after_split.split(' ') if n != ''] for after_split in nums.split('|')]
            winnings_nums_s = set(winning_nums)

            score = 0
            for n in my_nums:
                if n not in winnings_nums_s:
                    continue

                if score == 0:
                    score = 1
                else:
                    score *= 2

            ans += score


    print(ans)


def p2() -> None:
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

        n = len(lines)

        elf_rules_card_winnings = [0] * (n + 1)

        for i, line in enumerate(lines, 1):
            _, nums = line.split(':')

            winning_nums, my_nums = [[int(n) for n in after_split.split(' ') if n != ''] for after_split in nums.split('|')]
            winnings_nums_s = set(winning_nums)

            for num in my_nums:
                if num not in winnings_nums_s:
                    continue

                elf_rules_card_winnings[i] += 1
            
        copies_of_card = [1] * (n + 1)
        copies_of_card[0] = 0  # used for padding

        if DEBUG:
            print(elf_rules_card_winnings)

        for i, next_cards in enumerate(elf_rules_card_winnings):
            # probably optimizable
            for j in range(i + 1, min(n + 1, i + next_cards + 1)):  # wow. i forgot to pad `n` with `+ 1` here. 
                copies_of_card[j] += copies_of_card[i]

        if DEBUG:
            print(copies_of_card)
            

        print(sum(copies_of_card))

p2()

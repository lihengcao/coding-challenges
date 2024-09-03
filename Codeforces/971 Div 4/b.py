for _ in range(int(input())):
    rev_ans = []
    for _ in range(int(input())):
        rev_ans.append(input().index("#") + 1)

    for n in reversed(rev_ans):
        print(n, end=' ')
    print()

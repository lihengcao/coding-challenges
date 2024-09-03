"""Round 944"""

for _ in range(int(input())):
    word = list(input())

    for i in range(len(word) - 1):
        if word[i + 1] != word[i]:
            word[i], word[i + 1] = word[i + 1], word[i]
            print("yes")
            print("".join(word))
            break
    else:
        print("no")

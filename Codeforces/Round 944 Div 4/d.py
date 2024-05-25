"""Round 944"""

for _ in range(int(input())):
    stream = input()

    a = False
    count = 1

    for i in range(len(stream) - 1):
        if stream[i] != stream[i + 1]:
            if stream[i] == "0":
                a = True

            count += 1

    print(count - int(a is True))

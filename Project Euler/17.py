# power digit sum

for n in range(1, 16):
    print(1 << n, sum([int(c) for c in str(1 << n)]))

print(sum([int(c) for c in str(1 << 1000)]))

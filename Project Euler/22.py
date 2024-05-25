# Names scores

s = ""

with open("files/p022_names.txt", "r") as f:
    s = [w[1:-1] for w in f.readlines()[0].split(",")]

s.sort()

s = [sum(ord(c) - ord("A") + 1 for c in w) for w in s]

print(sum((i + 1) * n for i, n in enumerate(s)))

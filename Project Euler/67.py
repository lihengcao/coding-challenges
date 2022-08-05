# Maximum path sum II
s = None
with open("files/p067_triangle.txt", "r") as f:
    # in theory not good to load everything into memory, but it works
    s = f.read()


s = [l for l in s.split('\n') if l != ""]
for i in range(len(s)):
    if s[i] == "":
        continue
    s[i] = [int(n) for n in s[i].split()]
    
for r in range(len(s)-2, -1, -1):  # iterate backwards, excluding last row
    for c in range(len(s[r])):  # iterate through current row
        s[r][c] += max(s[r + 1][c], s[r + 1][c + 1])

print(s[0][0])
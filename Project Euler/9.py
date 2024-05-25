# brute force solution

for c in range(999):  # can't be 999 + 1 + 1
    for b in range(c):
        for a in range(b):
            if a + b + c > 1000:
                break
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print(a * b * c)

# slow way
ans = 0
upTo = 1000
for i in range(1,upTo):
    if i % 5 == 0 or i % 3 == 0:
        ans += i

print(ans)

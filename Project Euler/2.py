ans = 0
stopValue = 4_000_000
val1, val2 = 1, 2
while val2 < stopValue:
    if val2 & 1 == 0:
        ans += val2
    val1, val2 = val2, val1 + val2

print(ans)

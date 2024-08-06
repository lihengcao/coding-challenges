for _ in range(int(input())):
    s = list(input())
    t = input()


    cache = {}
    def solve(i_s, i_t) -> bool:
        # print(i_s, i_t)
        if i_t >= len(t):
            return True

        if i_s >= len(s):
            return False

        if (i_s, i_t) in cache:
            return cache[(i_s, i_t)]

        if s[i_s] == t[i_t]:
            a = solve(i_s + 1, i_t + 1)
            cache[(i_s, i_t)] = a
            return a

        if s[i_s] != '?':
            return False
        
        orig = s[i_s]
        s[i_s] = t[i_t]
        if solve(i_s + 1, i_t + 1):
            cache[(i_s, i_t)] = True
            return True
        s[i_s] = orig
        if solve(i_s + 1, i_t):
            cache[(i_s, i_t)] = True
            return True
        
        cache[(i_s, i_t)] = False
        return False

        
    if solve(0, 0):
        print("YES")
        print("".join(c if c != '?' else 'a' for c in s))
    else:
        print("NO")


    # i_s, i_t = 0, 0

    # while i_t < len(t):
    #     if s[i_s] == t[i_t]:
    #         i_s += 1
    #         i_t += 1
    #         continue

    #     if s[i_s] != '?':
    #         print("NO")
    #         break

    #     s[i_s] = t[i_t]
    #     i_s += 1
    #     i_t += 1
    # else:
    #     print("YES")
    #     print("".join(c if c != '?' else 'a' for c in s))




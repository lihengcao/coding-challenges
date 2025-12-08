for _ in range(int(input())):
    s = list(input())
    t = input()

    cache = {}

    def solve(
        s: str, t: str, cache: dict[tuple[int, int], bool], i_s: int, i_t: int
    ) -> bool:
        if i_t >= len(t):
            return True

        if i_s >= len(s):
            return False

        if (i_s, i_t) in cache:
            return cache[(i_s, i_t)]

        if s[i_s] == t[i_t]:
            a = solve(s, t, cache, i_s + 1, i_t + 1)
            cache[(i_s, i_t)] = a
            return a

        if solve(s, t, cache, i_s + 1, i_t):
            cache[(i_s, i_t)] = True
            return True

        if s[i_s] == "?":
            s[i_s] = t[i_t]
            if solve(s, t, cache, i_s + 1, i_t + 1):
                cache[(i_s, i_t)] = True
                return True
            s[i_s] = "?"

        cache[(i_s, i_t)] = False
        return False

    if solve(s, t, cache, 0, 0):
        print("YES")
        print("".join(c if c != "?" else "a" for c in s))
    else:
        print("NO")

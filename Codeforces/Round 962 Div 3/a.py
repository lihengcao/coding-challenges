for _ in range(int(input())):
    legs = int(input())

    ans = legs // 4 + legs % 4 // 2

    print(ans)
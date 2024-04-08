for _ in range(int(input())):
    n, k = [int(e) for e in input().split(' ')]

    arr = [int(e) for e in input().split(' ')]
    l, r = 0, len(arr) - 1

    while k and l < r and k >= 2 * min(arr[l], arr[r]):
        k -= 2 * min(arr[l], arr[r])

        if arr[l] == arr[r]:
            arr[l], arr[r] = 0, 0
            l += 1
            r -= 1
        elif arr[l] > arr[r]:
            arr[l] -= arr[r]
            arr[r] = 0
            r -= 1
        else:
            arr[r] -= arr[l]
            arr[l] = 0
            l += 1

    if l == r:
        if k >= arr[l]:
            arr[l] = 0
            l += 1
    else:
        if arr[l] <= arr[r]:
            if arr[l] * 2 - 1 == k:
                l += 1
        else:
            if arr[r] * 2 == k:
                r -= 1

    print(l + len(arr) - 1 - r)
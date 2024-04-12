for _ in range(int(input())):
    x, y = list(input()), list(input())

    if int(''.join(x)) < int(''.join(y)):
        x, y = y, x

    ind = 0

    while ind < len(x) and x[ind] == y[ind]:
        ind += 1
    ind += 1

    while ind < len(x):
        if int(x[ind]) > int(y[ind]):
            x[ind], y[ind] = y[ind], x[ind]
        ind += 1


    print(''.join(x))
    print(''.join(y))

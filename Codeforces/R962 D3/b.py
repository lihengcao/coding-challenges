for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    
    output_rows = n//k

    for _ in range(output_rows):
        input_row = list(input())
        output_row = []

        for i in range(0, n, k):
            output_row.append(input_row[i])

        for _ in range(k - 1):
            input()
        
        print("".join(output_row))
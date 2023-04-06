# lattic paths

table = [[None] * 21 for _ in range(21)]

def r(i: int, j: int) -> int:
    if i == 0 or j == 0:
        return 1
        
    if table[i][j] is None:
        table[i][j] = r(i - 1, j) + r(i, j - 1)
        
    return table[i][j]

    
print(r(20, 20))
day = 6
filename = f"{day}.txt"
# filename = f"{day}s.txt"
  

def search(size: int) -> int:
    with open(filename, "r") as f:
        for l in f.readlines():
            l = l.strip()
            
            for i in range(size - 1, len(l)):
                if len(set(list(l[i-size + 1:i+1]))) == size:
                    return i
    
    return -1


if __name__ == '__main__':
    print(search(4) + 1)
    print(search(14) + 1)

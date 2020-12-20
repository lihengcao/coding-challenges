# brute force way

def isPalindrome(n: int)-> bool:
    # ez
    return str(n)==str(n)[::-1]
    # same thing forwards and backwards

def generateProducts(start: int, stop: int)-> list[int]:
    ans = []
    for f1 in range(start, stop):
        for f2 in range(start,stop):
            ans.append(f1*f2)
    ans.sort(reverse=True)
    return ans


for e in generateProducts(100,1000):
    if isPalindrome(e):
        print(e)
        break


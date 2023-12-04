# 


filename = "input.txt"
filename = "sample.txt"


jets = open(filename, "r").readlines()[0]
print(jets)

rocks = [
    ["####"],
    [
        ".#.",
        "###",
        ".#."
    ],
    [
        "..#",
        "..#",
        "###",
    ],
    [
        "#",
        "#",
        "#",
        "#",
    ],
    {
        "##",
        "##",
    }
]

def check_intersection(cave: list[list[str]], rocks_ind: int, lower: int, left: int) -> bool:
    rock = rocks[rocks_ind]

    if lower + len(rock) >= 7:
        return False

    for rock_i in range(len(rock)):
        for rock_j in range(len(rock[0])):
            if cave[lower + rock_i][left + rock_j] == '#' == rock[rock_i][rock_j]:
                return True

    return False





def first() -> int:
    cave = [['.'] * 7 for _ in range(3)]
    highest = 0
    i_jet = 0
    for i in range(2022):
        if i % 100 == 0:
            print(i, end='\r')

        

        
    print()
        

    return highest


def second() -> int:
    return 0


if __name__ == '__main__':
    print(first())
    # print(second())

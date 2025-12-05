# 4.1
file = "input.txt"
input = list(map(list, open(file).read().splitlines()))

def solve1(input):
    size_x = len(input)
    size_y = len(input[0])
    total = 0
    for i in range(size_x):
        for j in range(size_y):
            if input[i][j] == '@':
                count = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if 0 <= i+k and i+k < size_x and 0 <= j+l and j+l < size_y:
                            if input[i+k][j+l] == '@':
                                count += 1
                if count <= 4:
                    total += 1
    return total

print(solve1(input))

# 4.2
file = "input.txt"
input = list(map(list, open(file).read().splitlines()))

def solve2(input):
    size_x = len(input)
    size_y = len(input[0])
    total = 0
    change = 1
    while change != 0:
        change = 0
        for i in range(size_x):
            for j in range(size_y):
                if input[i][j] == '@':
                    count = 0
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if 0 <= i+k and i+k < size_x and 0 <= j+l and j+l < size_y:
                                if input[i+k][j+l] == '@':
                                    count += 1
                    if count <= 4:
                        change += 1
                        input[i][j] = 'x'
        total += change
    return total

print(solve2(input))

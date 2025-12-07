from collections import defaultdict

file = "input.txt"
input = list(map(list, open(file).read().splitlines()))

def solve(input):
    s = input.pop(0).index('S')
    beams = defaultdict(int)
    beams[s] = 1
    size_y = len(input)
    for y in range(size_y):
        tmp = defaultdict(int)
        for b in beams.keys():
            c = input[y][b]
            count = beams[b]
            if c == '^':
                tmp[b-1] += count
                tmp[b+1] += count
            else:
                tmp[b] += count 
        beams = tmp.copy()
    return sum(beams.values())

print(solve(input))


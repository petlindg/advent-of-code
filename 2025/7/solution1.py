file = "input.txt"
input = list(map(list, open(file).read().splitlines()))

def solve(input):
    s = input.pop(0).index('S')
    beams = set()
    beams.add(s)
    size_x = len(input[0])
    size_y = len(input)
    count = 0
    for y in range(size_y):
        tmp = set()
        for b in beams:
            c = input[y][b]
            if c == '^':
                count += 1
                tmp.add(b-1)
                tmp.add(b+1)
            else:
                tmp.add(b)
        beams = tmp.copy()
    return count

print(solve(input))

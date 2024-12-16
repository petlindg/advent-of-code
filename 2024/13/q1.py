import re

def solve(e):
    ((ax, ay), (bx, by), (px, py)) = e
    ca = 0
    cb = 0
    solutions = []
    while px >= 0 and py >= 0:
        px -= bx
        py -= by
        cb += 1
    for _ in range(cb+1):
        if px == 0 and py == 0:
            solutions.append((ca, cb))
        px += bx
        py += by
        cb -= 1
        while px > 0 and py > 0:
            px -= ax
            py -= ay
            ca += 1
    if len(solutions)==0: return 0
    return max([a*3 + b for (a, b) in solutions])


f = open("input.txt", "r").read().split("\n\n")

data = []
for entry in f:
    e = list(map(int, re.findall("[0-9]+", entry)))
    data.append(((e[0], e[1]), (e[2], e[3]), (e[4], e[5])))

print(sum([solve(e) for e in data]))
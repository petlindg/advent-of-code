import re

def solve(e):
    (ax, ay, bx, by, px, py) = e
    
    ### elim second row a
    py = py*ax-px*ay
    by = by*ax-bx*ay
    ay = ay*ax-ax*ay

    ### reduce second row b
    if py%by!=0: return 0
    py = py//by
    by //= by

    ### sub first row b
    px = px-bx*py
    bx = bx-bx

    ### reduce first row a
    if px%ax!=0: return 0
    px = px//ax
    ax = 1

    return px*3+py

f = open("input.txt", "r").read().split("\n\n")

data = []
for entry in f:
    e = list(map(int, re.findall("[0-9]+", entry)))
    data.append((e[0], e[1], e[2], e[3], e[4]+10000000000000, e[5]+10000000000000))

print(sum([solve(e) for e in data]))
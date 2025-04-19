from functools import cache
import re
import heapq

def distance(x1, y1, x2, y2):
    return abs(y2-y1)+abs(x2-x1)

def getmap(mats):
    d = dict()
    for m in mats:
        for i in range(len(m)):
            for j in range(len(m[0])):
                c = m[i][j]
                if c != None:
                    d[c] = (i, j)
    return d

@cache
def move(sx, sy, ex, ey):
    seq1 = []
    seq2 = []
    dx = ex-sx
    dy = ey-sy
    if dx > 0:
        cx = 'v'
    else:
        cx = '^'
    if dy > 0:
        cy = '>'
    else:
        cy = '<'
    seq1 += abs(dx)*cx + abs(dy)*cy + "A"
    seq2 += abs(dy)*cy + abs(dx)*cx + "A"
    if dx==0 or dy==0:
        return [seq1]
    else:
        return [seq1, seq2]

def solve(code):
    numpad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'B']]
    dirpad = [[None, '^', 'A'], ['<', 'v', '>']]
    m = getmap([numpad, dirpad])
    num = int(code[0:3])
    s = code
    imax = 3
    nodes = []
    nodes.append((0, 0, 0, s, [], (3, 2)))
    while len(nodes) != 0:
        (v, i, j, s, sb, (sx, sy)) = heapq.heappop(nodes)
        if i==imax:
            return num*len(s)
        if j == len(s):
            nodes = [(v, i+1, 0, sb, [], (0, 2))]
            #heapq.heappush(nodes, (v, i+1, 0, sb, [], (0, 2)))
        else:
            c = s[j]
            (ex, ey) = m[c]
            st = move(sx, sy, ex, ey)
            if len(st)==2:
                s2 = sb.copy()
                s2 += st[1]
                heapq.heappush(nodes, (v+1, i, j+1, list(s), s2, (ex, ey)))
            sb += st[0]
            heapq.heappush(nodes, (v+1, i, j+1, list(s), sb, (ex, ey)))
    print("No sequence found")
    return num*len(s)

def solveAll(codes):
    v = 0
    for c in codes:
        vt = solve(c)
        print(vt)
        v += vt
    return v

codes = re.sub("A", "B", open("test.txt", "r").read()).split('\n')

print(solveAll(codes))

#print(solve(codes[0]))

# 029A
# 980A
# 179A
# 456A
# 379A

#+---+---+---+
#| 7 | 8 | 9 |
#+---+---+---+
#| 4 | 5 | 6 |
#+---+---+---+
#| 1 | 2 | 3 |
#+---+---+---+
#    | 0 | A |
#    +---+---+

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
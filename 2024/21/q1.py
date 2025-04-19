from functools import cache
import re

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
    ss = [[code]]
    pads = [(3, 2)] + [(0, 2)]
    mi = len(pads)-1
    for i in range(len(pads)):
        print(i, ss)
        ss.append([])
        for s in ss[i]:
            print(i, s)
            for c in s:
                (sx, sy) = pads[i]
                (ex, ey) = m[c]
                ss[i+1] += move(sx, sy, ex, ey)
                #print(ss[i+1])
                pads[i] = (ex, ey)
    ss[mi].sort(key=(lambda x: len(x)), reverse=True)
    s = ss[mi].pop()
    print(ss)
    print(s)
    return int(code[0:3])*len(s)


codes = re.sub("A", "B", open("test.txt", "r").read()).split('\n')

print(solve(codes[0]))

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
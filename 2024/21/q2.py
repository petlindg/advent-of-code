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

def solver(m, mm:dict, s, sx, sy, i):
    if i==0: return s
    sb = []
    for c in s:
        t = False
        for j in range(i, 0, -1):
            if (c, j) in mm:
                t = mm[(c, j, sx, sy)]
                break
        if t==False:
            (ex, ey) = m[c]
            ns = move(sx, sy, ex, ey)
            sbt = min([solver(m, mm, ns[k], 0, 2, i-1) for k in range(len(ns))])
            mm[(c, i, sx, sy)] = (sbt, sx, sy)
            (sx, sy) = (ex, ey)
        else:
            (sbt, sx, sy) = t
        sb += sbt
    return sb

def solve(code):
    numpad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'B']]
    dirpad = [[None, '^', 'A'], ['<', 'v', '>']]
    m = getmap([numpad, dirpad])
    mm = dict()
    mm.setdefault(lambda x: False)
    num = int(code[0:3])
    s = list(code)
    sr = solver(m, mm, s, 3, 2, 15)
    print(num, len(sr))
    print(''.join(sr))
    return len(sr)*num


def solveAll(codes):
    v = 0
    for c in codes:
        vt = solve(c)
        print(vt)
        v += vt
    return v

codes = re.sub("A", "B", open("input.txt", "r").read()).split('\n')

print(solveAll(codes))
#print(solve(codes[0]))
#carr(3, 2, 3, 2, 26)
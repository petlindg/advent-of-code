import re
from functools import reduce
from operator import mul

def solve(robots, h, w, time):
    q = [0, 0, 0, 0]
    for (px, py, vx, vy) in robots:
        px = (px+time*vx)%h
        py = (py+time*vy)%w
        if px<h//2:
            if py<w//2:
                q[0]+=1
            elif py>w//2:
                q[1]+=1
        elif px>h//2:
            if py<w//2:
                q[2]+=1
            elif py>w//2:
                q[3]+=1
    return reduce(mul, q)


f = open("input.txt", "r").read().split('\n')
robots = [list(map(int, (re.sub("[p|v]+=", "", re.sub(",", " ", s))).split(' '))) for s in f]
print(solve(robots, 101, 103, 100))
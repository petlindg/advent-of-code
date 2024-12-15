import re

def printRobots(robots, h, w):
    arr = [['.' for _ in range(w)] for _ in range(h)]
    for (px, py, vx, vy) in robots:
        arr[px][py] = '1'
    [print(''.join(l)) for l in arr]

def solve(robots, h, w):
    time = 0
    dirs = [(-1, -1), (-1, 0),(-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    nmax = 0
    tmax = 0
    # cycles on 10403
    while time < 10403:
        for i in range(len(robots)):
            (px, py, vx, vy) = robots[i]
            robots[i][0] = (px+vx)%h
            robots[i][1] = (py+vy)%w
        time += 1
        n = 0
        d = [(x, y) for (x, y, _, _) in robots]
        for (px, py, vx, vy) in robots:
            for (dx, dy) in dirs:
                if (px+dx, py+dy) in d:
                    n+=1
        if n > nmax:
            nmax = n
            tmax = time
    return tmax


f = open("input.txt", "r").read().split('\n')
robots = [list(map(int, (re.sub("[p|v]+=", "", re.sub(",", " ", s))).split(' '))) for s in f]
print(solve(robots, 101, 103))
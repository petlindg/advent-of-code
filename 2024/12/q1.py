from collections import defaultdict

def inBounds(room, x, y):
    h = len(room)
    w = len(room[0])
    return 0 <= x and x < h and 0 <= y and y < w

def fence(room):
    h = len(room)
    w = len(room[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cmap = defaultdict(int)
    pmap = defaultdict(lambda: (0,0))
    visited = []
    for i in range(h):
        for j in range(w):
            if (i, j) not in visited:
                current = [(i, j)]
                arr = [(i, j)]
                e = room[i][j]
                a = 0
                pe = 0
                while len(arr) != 0:
                    (x, y) = arr.pop()
                    a += 1
                    for (dx, dy) in dirs:
                        nx = x+dx
                        ny = y+dy
                        if inBounds(room, nx, ny) and e == room[nx][ny] and (nx, ny) not in current:
                            arr.append((nx, ny))
                            current.append((nx, ny))
                        elif (nx, ny) not in current:
                            pe += 1
                visited += current
                pmap[str(e) + str(cmap[e])] = (a, pe)
                cmap[e] += 1
    return pmap
                        
                    
room = [list(line) for line in open("test3.txt", "r").read().split('\n')]
pmap = fence(room)
cost = sum([a*pe for (a, pe) in pmap.values()])

[print("k:" + str(k) + " a:" + str(pmap[k][0]) + " :pe" + str(pmap[k][1])) for (k) in pmap.keys()]

print(cost)

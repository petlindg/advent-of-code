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
                edges = []
                e = room[i][j]
                while len(arr) != 0:
                    (x, y,) = arr.pop()
                    for (dx, dy) in dirs:
                        nx = x+dx
                        ny = y+dy
                        if inBounds(room, nx, ny) and e == room[nx][ny] and (nx, ny) not in current:
                            arr.append((nx, ny))
                            current.append((nx, ny))
                        elif (nx, ny) not in current:
                            edges.append((x, y, dx, dy))
                pe = 0
                while len(edges)!=0:
                    e = edges.pop()
                    tmp = [e]
                    while len(tmp)!=0:
                        (x, y, ddx, ddy) = tmp.pop()
                        for (dx, dy) in dirs:
                            ce = (x+dx, y+dy, ddx, ddy)
                            if ce in edges:
                                edges.remove(ce)
                                tmp.append(ce)
                    pe += 1
                a = len(current)
                visited += current
                pmap[str(e) + str(cmap[e])] = (a, pe)
                cmap[e] += 1
    return pmap
                        
                    
room = [list(line) for line in open("input.txt", "r").read().split('\n')]
pmap = fence(room)
cost = sum([a*pe for (a, pe) in pmap.values()])
print(cost)
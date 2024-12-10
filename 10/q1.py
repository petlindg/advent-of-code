def inBounds(room, x, y):
    h = len(room)
    w = len(room[0])
    return 0 <= x and x < h and 0 <= y and y < w

def path (room, x, y):
    dsts = []
    dirs = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    e1 = room[x][y]
    for (i, j) in dirs:
        if inBounds(room, i, j):
            e2 = room[i][j] 
            if e2==e1+1:
                if e2 == 9:
                    dsts.append((i, j))
                else:
                    dsts += path(room, i, j)
    return dsts

def score(room):
    h = len(room)
    w = len(room[0])
    r = 0
    for x in range(h):
        for y in range(w):
            if room[x][y] == 0:
                
                r += len(set(path(room, x, y)))
    return r



room = [list(map(int, line)) for line in open("input.txt", "r").read().split('\n')]

r = score(room)

print(r)


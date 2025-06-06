import heapq

def inBounds(room, x, y):
    h = len(room)
    w = len(room[0])
    return 0 <= x and x < h and 0 <= y and y < w

def bfs(room):
    (x, y) = (0, 0)
    end = (len(room)-1, len(room[0])-1)
    visited = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    nodes = []
    heapq.heappush(nodes, (0, (x, y)))
    while len(nodes) != 0:
        (v, (x, y)) = heapq.heappop(nodes)
        if (x, y) == end:
            return v
        for d in dirs:
            (dx, dy) = d
            nx = x+dx
            ny = y+dy
            if inBounds(room, nx, ny):
                ne = room[nx][ny]
                if ne != '#' and (nx, ny) not in visited:
                    visited.append((nx, ny))
                    heapq.heappush(nodes, ((v+1, (nx, ny))))

def fill(room, coords, n):
    for i in range(n):
        (x, y) = coords[i]
        room[x][y] = '#'


l = 71
room = [['.' for _ in range(l)] for _ in range(l)]

[print(''.join(l)) for l in room]

coords = [(int(l.split(',')[1]), int(l.split(',')[0])) for l in open("input.txt", "r").read().split('\n')]

fill(room, coords, 1024)

[print(''.join(l)) for l in room]

print(bfs(room))
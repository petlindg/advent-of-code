
def findChar(room, c):
    h = len(room)
    w = len(room[0])
    for x in range(h):
        for y in range(w):
            if room[x][y] == c:
                return (x, y)

def bfs(room):
    end = findChar(room, 'E')
    (x, y) = findChar(room, 'S')
    visited = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    nodes = []
    nodes.append((0, (x, y, (0, 1))))
    while len(nodes) != 0:
        (v, (x, y, od)) = nodes.pop()
        if (x, y) == end:
            return v
        for d in dirs:
            (dx, dy) = d
            nx = x+dx
            ny = y+dy
            ne = room[nx][ny]
            if ne != '#' and (nx, ny, d) not in visited:
                if d == od:
                    visited.append((nx, ny, d))
                    nodes.append((v+1, (nx, ny, d)))
                else:
                    visited.append((x, y, d))
                    nodes.append((v+1000, (x, y, d)))
        nodes.sort(reverse=True)


room = list(map(list, open("input.txt", "r").read().split('\n')))

print(bfs(room))
[print(''.join(l)) for l in room]
from copy import deepcopy

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
    nodes.append((0, [(x, y)], (x, y, (0, 1))))
    while len(nodes) != 0:
        (v, p, (x, y, od)) = nodes.pop()
        if (x, y)==end:
            w = v
            pt = p
            while v == w:
                (v, p, (x, y, od)) = nodes.pop()
                if (x, y)==end:
                    pt += p
            return set(pt)
        for d in dirs:
            (dx, dy) = d
            nx = x+dx
            ny = y+dy
            ne = room[nx][ny]
            if ne != '#':
                if (nx, ny, d) not in visited:
                    if d == od:
                        nodes.append((v+1, p+[(nx, ny)], (nx, ny, d)))
                        visited.append((nx, ny, d))
                    else:
                        nodes.append((v+1000, p, (x, y, d)))
                        visited.append((x, y, d))
                elif d == od and any([a==v+1 and b==(nx, ny, d) for (a, _, b) in nodes]):
                    nodes.append((v+1, p+[(nx, ny)], (nx, ny, d)))
                    visited.append((nx, ny, d))
                elif any([a==v+1000 and b==(nx, ny, d) for (a, _, b) in nodes]):
                    nodes.append((v+1000, p, (x, y, d)))
                    visited.append((x, y, d))
        nodes.sort(reverse=True)


room = list(map(list, open("input.txt", "r").read().split('\n')))

nodes = bfs(room)
for (x, y) in nodes:
    room[x][y] = 'O'
[print(''.join(l)) for l in room]
print(len(nodes))
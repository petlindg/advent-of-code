import heapq

def findChar(room, c):
    h = len(room)
    w = len(room[0])
    for x in range(h):
        for y in range(w):
            if room[x][y] == c:
                return (x, y)

def inBounds(room, x, y):
    h = len(room)
    w = len(room[0])
    return 0 <= x and x < h and 0 <= y and y < w

def bfs(room, start, end):
    visited = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    nodes = []
    heapq.heappush(nodes, (0, start))
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
    return None

def ccarr(room, start):
    carr = [['#' for _ in range(len(room[0]))]for _ in range(len(room))]
    carr[start[0]][start[1]] = 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = []
    visited.append(start)
    nodes = []
    heapq.heappush(nodes, (0, start))
    while len(nodes) != 0:
        (v, (x, y)) = heapq.heappop(nodes)
        for d in dirs:
            (dx, dy) = d
            nx = x+dx
            ny = y+dy
            if inBounds(room, nx, ny):
                ne = room[nx][ny]
                if ne != '#' and (nx, ny) not in visited:
                    visited.append((nx, ny))
                    carr[nx][ny] = v+1
                    heapq.heappush(nodes, ((v+1, (nx, ny))))
    return carr

def cheat(room, start, end, carr, maxVal):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    skips = set()
    nodes = []
    nodes.append((0, start))
    visited = []
    visited.append(start)
    while len(nodes) != 0:
        (v, (x, y)) = nodes.pop()
        if v > maxVal: continue
        for (dx, dy) in dirs:
            nx = x+dx
            ny = y+dy
            np = (nx, ny)
            if inBounds(room, nx, ny) and np not in visited:
                ne = room[nx][ny]
                if ne == '#':
                    for (ddx, ddy) in dirs:
                        nnx = nx+ddx
                        nny = ny+ddy
                        nnp = (nnx, nny)
                        if inBounds(room, nnx, nny) and room[nnx][nny] != '#':
                            if carr[nnx][nny]+v+2<=maxVal:
                                skips.add((np, nnp))
                elif ne != '#':
                    visited.append(np)
                    heapq.heappush(nodes, (v+1, np))
    return len(skips)

def solve(room):
    start = findChar(room, 'S')
    end = findChar(room, 'E')
    carr = ccarr(room, end)
    maxVal = carr[start[0]][start[1]]-100
    print(maxVal)
    count = cheat(room, start, end, carr, maxVal)
    return count

room = list(map(list, open("input.txt", "r").read().split('\n')))
print(solve(room))
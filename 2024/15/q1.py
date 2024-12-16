def tryMove(room, x, y, d, c):
    (dx, dy) = d
    nx = x+dx
    ny = y+dy
    e = room[nx][ny]
    if e == '#':
        return False
    elif e == '.':
        room[nx][ny] = c
        return True
    elif e == 'O':
        if tryMove(room, nx, ny, d, e):
            room[nx][ny] = c
            return True
        return False
    
def getDir(c):
    if c == '^':
        return (-1, 0)
    elif c == '>':
        return (0, 1)
    elif c == 'v':
        return (1, 0)
    elif c == '<':
        return (0, -1)

def move(room, x, y, m):
    d = getDir(m)
    (dx, dy) = d
    if tryMove(room, x, y, d, '@'):
        room[x][y] = '.'
        return (x+dx, y+dy)
    return (x, y)

def findRobot(room):
    h = len(room)
    w = len(room[0])
    for x in range(h):
        for y in range(w):
            if room[x][y] == '@':
                return (x, y)

def solve(room, moves):
    (x, y) = findRobot(room)
    for m in moves:
        (x, y) = move(room, x, y, m)
    r = 0
    for x in range(len(room)):
        for y in range(len(room[0])):
            if room[x][y] == 'O':
                r += x*100+y
    return r

f = open("input.txt", "r").read().split("\n\n")
room = list(map(list, f[0].split('\n')))
moves = ''.join(f[1].split('\n'))

print(solve(room, moves))
def checkMove(room, x, y, d, c):
    (dx, dy) = d
    nx = x+dx
    ny = y+dy
    e = room[nx][ny]
    if e == '#':
        return False
    elif e == '.':
        return True
    elif dx != 0:
        if e == '[':
            return checkMove(room, nx, ny, d, e) and checkMove(room, nx, ny+1, d, ']')
        elif e == ']':
            return checkMove(room, nx, ny, d, e) and checkMove(room, nx, ny-1, d, '[')
    else:
        return checkMove(room, nx, ny, d, e)

def move1(room, x, y, d, c):
    (dx, dy) = d
    nx = x+dx
    ny = y+dy
    e = room[nx][ny]
    if e == '#':
        return False
    elif e == '.':
        room[nx][ny] = c
        return True
    elif dx != 0:
        if e == '[':
            move1(room, nx, ny, d, e)
            move1(room, nx, ny+1, d, ']')
            room[nx][ny] = c
            room[nx][ny+1] = '.'
        elif e == ']':
            move1(room, nx, ny, d, e)
            move1(room, nx, ny-1, d, '[')
            room[nx][ny] = c
            room[nx][ny-1] = '.'
    else:
        move1(room, nx, ny, d, e)
        room[nx][ny] = c
    
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
    if checkMove(room, x, y, d, '@'):
        move1(room, x, y, d, '@')
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
            if room[x][y] == '[':
                r += x*100+y
    return r

def expand(room):
    newRoom = [['.']*len(l)*2 for l in room]
    for x in range(len(room)):
        for y in range(len(room[0])):
            e = room[x][y]
            if e == '#':
                newRoom[x][y*2] = '#'
                newRoom[x][y*2+1] = '#'
            if e == 'O':
                newRoom[x][y*2] = '['
                newRoom[x][y*2+1] = ']'
            if e == '@':
                newRoom[x][y*2] = '@'
    return newRoom

f = open("input.txt", "r").read().split("\n\n")
room = list(map(list, f[0].split('\n')))
room = expand(room)
moves = ''.join(f[1].split('\n'))

print(solve(room, moves))
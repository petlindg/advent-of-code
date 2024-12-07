from enum import Enum
from copy import deepcopy
import sys
sys.setrecursionlimit(10000)

class Direction(Enum):
    UP    = (-1, 0)
    RIGHT = (0, 1)
    DOWN  = (1, 0)
    LEFT  = (0, -1)
    def next(self):
        if self == Direction.UP:
            return Direction.RIGHT
        elif self == Direction.RIGHT:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.LEFT
        elif self == Direction.LEFT:
            return Direction.UP
    def __eq__(self, o):
        return self.value == o.value

def findGuard(room):
    directions = "^>v<"
    for i in range(len(room)):
        for j in range(len(room[i])):
            if room[i][j] in directions:
                return (i, j)

def getDirection(c):
    if c == '^':
        return Direction.UP
    elif c == '>':
        return Direction.RIGHT
    elif c == 'v':
        return Direction.DOWN
    elif c == '<':
        return Direction.LEFT
    else:
        raise RuntimeError("Invalid direction in getDirection")


def getPath(room, x, y, direction:Direction):
    (i, j) = direction.value
    new_x = x + i
    new_y = y + j
    if new_x < 0 or new_x > (len(room)-1) or new_y < 0 or new_y > (len(room[0])-1):
        return [(x, y)]
    if room[new_x][new_y] == '#':
        return getPath(room, x, y, direction.next())
    else:
        return [(x, y)] + getPath(room, new_x, new_y, direction)

def loops(room, x, y, direction:Direction):
    path = []
    while True:
        (i, j) = direction.value
        new_x = x + i
        new_y = y + j
        if (x, y, direction) in path:
            return 1
        path.append((x, y, direction))
        if new_x < 0 or new_x > (len(room)-1) or new_y < 0 or new_y > (len(room[0])-1):
            return 0
        if room[new_x][new_y] == '#':
            direction = direction.next()
        else:
            x = new_x
            y = new_y

def getPlacements(room, i, j, direction, positions):
    placements = []
    for (x, y) in positions:
        print(str(x) + str(y))
        if (x, y) != (i, j):
            room[x][y] = '#'
            if loops(room, i, j, direction):
                placements.append((x,y))
            room[x][y] = '.'
    return placements

room = [list(line) for line in open("input.txt", "r").read().split('\n')]
#room = [list(line) for line in open("test.txt", "r").read().split('\n')]

(x, y) = findGuard(room)
direction = getDirection(room[x][y])
path = getPath(room, x, y, direction)
positions = list(set(path))
loopPositions = getPlacements(room, x, y, direction, positions)
print(len(loopPositions))
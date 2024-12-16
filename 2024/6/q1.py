from enum import Enum
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

def move(room, x, y, direction:Direction):
    (i, j) = direction.value
    new_x = x + i
    new_y = y + j
    if new_x < 0 or new_x > (len(room)-1) or new_y < 0 or new_y > (len(room[0])-1):
        return [(x, y)]
    if room[new_x][new_y] == '#':
        return move(room, x, y, direction.next())
    else:
        return [(x, y)] + move(room, new_x, new_y, direction)

room = [list(line) for line in open("input.txt", "r").read().split('\n')]

(x, y) = findGuard(room)
direction = getDirection(room[x][y])
path = move(room, x, y, direction)
positions = list(set(path))
print(len(positions))
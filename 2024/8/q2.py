from math import gcd

def inBounds(room, x, y):
    h = len(room)
    w = len(room[0])
    return x >= 0 and x < h and y >= 0 and y < w

def getNodes(room):
    h = len(room)
    w = len(room[0])
    nodes = set()
    for x1 in range(h):
        for y1 in range(w):
            c1 = room[x1][y1]
            if c1 != '.':
                for x2 in range(h):
                    for y2 in range(w):
                        c2 = room[x2][y2]
                        if c2 == c1 and (x1 != x2 and y1 != y2):
                            dx = x2-x1
                            dy = y2-y1
                            d = gcd(dx, dy)
                            dx //= d
                            dy //= d

                            x = x1
                            y = y1
                            while inBounds(room, x-dx, y-dy):
                                x-=dx
                                y-=dy

                            while inBounds(room, x, y):
                                nodes.add((x, y))
                                x+=dx
                                y+=dy
    return nodes

room = [line for line in open("input.txt", "r").read().split()]

nodes = getNodes(room)

print(len(nodes))
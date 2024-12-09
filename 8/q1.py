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
                            mnodes = []

                            px1 = x1-dx
                            py1 = y1-dy
                            mnodes.append((px1, py1))

                            if dx%3==0 and dy%3==0:
                                px2 = x1+dx//3
                                py2 = y1+dy//3
                                mnodes.append((px2, py2))
                            
                            px3 = x2+dx
                            py3 = y2+dy
                            mnodes.append((px3, py3))

                            for (m, n) in mnodes:
                                if inBounds(room, m, n):
                                    nodes.add((m, n))
    return nodes

room = [line for line in open("input.txt", "r").read().split()]

nodes = getNodes(room)

print(len(nodes))
import math
from collections import defaultdict

file = 'input.txt'
input = [tuple(map(int, l.split(','))) for l in open(file).read().splitlines()]

def distance(e):
    p1, p2 = e
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return d

def solve(input):
    count = 1000
    size = len(input)
    edges = []
    for i in range(size):
        for j in range(i+1, size):
            edges.append((input[i], input[j]))
    edges.sort(key=distance)
    connections = edges[0:count]
    nodes = input

    buffer = [nodes.pop()]
    graph = []
    lengths = []
    visited = []
    while True:
        n = buffer.pop()
        for (p1, p2) in connections:
            if n==p1 and p2 not in visited:
                buffer.append(p2)
                graph.append(p2)
                visited.append(p2)
                if p2 in nodes:
                    nodes.remove(p2)
            if n==p2 and p1 not in visited:
                buffer.append(p1)
                graph.append(p1)
                visited.append(p1)
                if p1 in nodes:
                    nodes.remove(p1)
        if len(nodes)==0:
            break
        if len(buffer)==0:
            lengths.append(len(graph))
            graph = []
            buffer = [nodes.pop()]
    lengths.sort(reverse=True)
    return math.prod(lengths[:3])

print(solve(input))

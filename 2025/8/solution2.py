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
    size = len(input)
    edges = []
    for i in range(size):
        for j in range(i+1, size):
            edges.append((input[i], input[j]))
    edges.sort(key=distance)
    nodes = input

    graph = set()
    x1 = 0
    x2 = 0
    while len(graph) < len(nodes):
        p1, p2 = edges.pop(0)
        x1 = p1[0]
        x2 = p2[0]
        graph.add(p1)
        graph.add(p2)
    return x1*x2

print(solve(input))

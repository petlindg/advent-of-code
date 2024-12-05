import sys

def c2(ls:list, m:list):
    tra = []
    for i in range(len(ls)):
        for t in tra:
            if t in m[ls[i]]:
                tmp = ls[i]
                ls[i] = ls[i-1]
                ls[i-1] = tmp
                return c2(ls, m)
        tra.append(ls[i])
    return ls[len(ls)//2]


def c(ls:list, m:list):
    traversed = []
    for e in ls:
        for t in traversed:
            if t in m[e]:
                return c2(ls, m)
        traversed.append(e)
    return 0

f = open("input.txt", "r").read().split("\n\n")
specs = f[0].split('\n')
xs = f[1].split('\n')

a = [[] for i in range(100)]

for l in specs:
    l = l.split('|')
    k = int(l[0])
    e = int(l[1])
    for i in range(100):
        if i==k:
            a[i] += [e]


print(sum([c(list(map(int, x.split(','))), a) for x in xs]))
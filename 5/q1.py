def c(ls:list, m:list):
    ls = list(map(int, ls.split(',')))
    traversed = []
    for e in ls:
        for t in traversed:
            if t in m[e]:
                return 0
        traversed.append(e)
    return ls[len(ls)//2]

f = open("input.txt", "r").read().split("\n\n")
#f = open("test1.txt", "r").read().split("\n\n")
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


print(sum([c(x, a) for x in xs]))
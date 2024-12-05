

def distance(l1, l2):
    r = 0
    for (x, y) in zip(l1, l2):
        r += abs(x-y)
    return r

def decSafe1(xs):
    last = xs[0]
    l = len(xs)
    for i in range(1, l):
        x = xs[i]
        if x>last or x+3<last:
            return 0
        last = x
    return 1

def decSafe(xs):
    last = xs[0]
    l = len(xs)
    for i in range(1, l):
        x = xs[i]
        if x>=last or x+3<last:
            return decSafe1([last] + xs[i+1:l])
        last = x
    return 1

def incSafe1(xs):
    last = xs[0]
    l = len(xs)
    for i in range(1, l):
        x = xs[i]
        if x<=last or x>last+3:
            return 0
        last = x
    return 1

def incSafe(xs):
    last = xs[0]
    l = len(xs)
    for i in range(1, l):
        x = xs[i]
        if x<=last or x>last+3:
            return incSafe1([last] + xs[i+1:l])
        last = x
    return 1


def safe(xs):
    l = len(xs)
    return max([decSafe(xs), incSafe(xs), decSafe1(xs[1:l]), incSafe1(xs[1:l])])

xs = open("input1.txt", "r").read().split('\n')

xs = [list(map(int, x.split(" "))) for x in xs]

# xs = [[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9],[10,4,3,2,1],[0,8,9,10],[0,8,9,5],[10,5,4,0]]

r=sum([safe(x) for x in xs])

print(r)
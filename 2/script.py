

def distance(l1, l2):
    r = 0
    for (x, y) in zip(l1, l2):
        r += abs(x-y)
    return r

def decSafe1(last, xs):
    for i in range(len(xs)):
        x = xs[i]
        if x>last or x+3<last:
            return 0
        last = x
    return 1

def decSafe(xs):
    last = xs[0]
    for i in range(1, len(xs)):
        x = xs[i]
        if x>=last or x+3<last:
            return decSafe1(last, xs[i+1:len(xs)])
        last = x
    return 1

def incSafe1(last, xs):
    for i in range(len(xs)):
        x = xs[i]
        if x<=last or x>last+3:
            return 0
        last = x
    return 1

def incSafe(xs):
    last = xs[0]
    for i in range(1, len(xs)):
        x = xs[i]
        if x<=last or x>last+3:
            return incSafe1(last, xs[i+1:len(xs)])
        last = x
    return 1


def safe(xs):
    l = len(xs)
    return max([decSafe(xs), incSafe(xs), decSafe1(xs[1], xs[2:l]), incSafe1(xs[1], xs[2:l])])

xs = open("input.txt", "r").read().split('\n')

xs = [list(map(int, x.split(" "))) for x in xs]

#xs = [[7,6,4,2,1], [1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9], [20,5,4,3,2], [6, 20, 5, 4, 3, 2], [20, 19, 22, 24, 22], [20, 22, 19, 16, 15], [2, 0, 4, 6, 8], [0, 4, 6, 8],
#      [2, 4, 6, 8, 6], [8, 6, 2, 0], [8, 5, 0, 2], [0, 9, 6, 4], [3, 5, 7, 6], [0, 10, 8, 11]]

r=sum([safe(x) for x in xs])

print(r)
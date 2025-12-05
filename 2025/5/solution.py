# 5.1
file = "input.txt"
input = open(file).read().split("\n\n")
fresh = [(int(e.split('-')[0]), int(e.split('-')[1])) for e in input[0].splitlines()]
available = list(map(int, input[1].splitlines()))
def solve1(fresh, available):
    fresh.sort()
    available.sort()
    count = 0
    a = -1
    while len(fresh)!=0:
        (s, e) = fresh.pop(0)
        while a<s and len(available)!=0:
            a = available.pop(0)
        while a<=e and len(available)!=0:
            a = available.pop(0)
            count += 1
    return count
print(solve1(fresh, available))

# 5.2
file = "input.txt"
input = open(file).read().split("\n\n")
fresh = [(int(e.split('-')[0]), int(e.split('-')[1])) for e in input[0].splitlines()]

def solve2(fresh):
    fresh.sort()
    count = 0
    while len(fresh) != 0:
        start, end = fresh.pop(0)
        while len(fresh)!=0 and fresh[0][0]<=end:
            end = max(fresh.pop(0)[1], end)
        count += end-start+1
    return count 

print(solve2(fresh))

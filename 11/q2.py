from collections import defaultdict

def blink(stonemap:defaultdict):
    arr = []
    for st in stonemap.keys():
        c = stonemap[st]
        stonemap[st] -= c
        s = str(st)
        l = len(s)
        if st == 0:
            arr.append((1, c))
        elif l%2==0:
            arr.append((int(s[0:l//2]), c))
            arr.append((int(s[l//2:l]), c))
        else:
            arr.append((st*2024, c))
    for (s, c) in arr:
        stonemap[s] += c

stones = list(map(int, open("input.txt", "r").read().split(' ')))
b = 75
stonemap = defaultdict(int)
for s in stones:
    stonemap[s]+=1
[blink(stonemap) for _ in range(b)]
stonesum = sum(stonemap.values())
print(stonesum)


def det(patterns, design):
    l = len(design)
    maxP = max(list(map(len, patterns)))
    arr = [False for _ in range(l)]
    arr[0] = True
    for i in range(l):
        s = i-min(i, maxP)
        for j in range(s, i+1):
            for p in patterns:
                if p==design[j:i] and arr[j]:
                    arr[i] = True
    return arr[l-1]
            
def countValid(patterns, designs):
    return sum([det(patterns, d) for d in designs])

f = open("input.txt", "r").read().split("\n\n")
patterns = f[0].split(", ")
designs = f[1].split('\n')

print(countValid(patterns, designs))

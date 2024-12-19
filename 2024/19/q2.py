def perms(patterns, design):
    l = len(design)
    maxP = max(list(map(len, patterns)))
    arr = [0 for _ in range(l+1)]
    arr[0] = 1
    for i in range(l+1):
        s = i-min(i, maxP)
        for j in range(s, i+1):
            for p in patterns:
                if p==design[j:i]:
                    arr[i] += arr[j]
    return arr[l]
            
def countValid(patterns, designs):
    return sum([perms(patterns, d) for d in designs])

f = open("input.txt", "r").read().split("\n\n")
patterns = f[0].split(", ")
designs = f[1].split('\n')

print(countValid(patterns, designs))
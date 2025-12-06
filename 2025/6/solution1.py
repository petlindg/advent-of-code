import math

file = "input.txt"
input = open(file).read().splitlines()

def parse_nums(l):
    nl = []
    b = ""
    for i, e in enumerate(l):
        if e==' ':
            if b!="":
                nl.append(int(b))
            b = ""
        else:
            b += e
            if i==len(l)-1:
                nl.append(int(b))
    return nl

def parse_ops(l):
    nl = []
    for i, e in enumerate(l):
        if e==' ':
            continue
        else:
            nl.append(e)
    return nl

def solve(nums, ops):
    s = 0
    for i, op in enumerate(ops):
        tmp = [e[i] for e in nums]
        if op=='+':
            s += sum(tmp)
        else:
            s += math.prod(tmp) 
    return s

ops = parse_ops(input.pop(-1))
nums = list(map(parse_nums, input))

print(solve(nums, ops))

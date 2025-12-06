import math

file = "input.txt"
input = open(file).read().splitlines()

def solve(input):
    y = len(input)
    x = len(input[0])
    b = []
    s = 0
    for j in range(x-1, -1, -1):
        sb = ""
        for i in range(y):
            c = input[i][j]
            if c == '+':
                b.append(int(sb))
                sb = ""
                s += sum(b)
                print(b)
                b = []
            elif c == '*':
                b.append(int(sb))
                sb = ""
                s += math.prod(b)
                print(b)
                b = []
            elif c.isdigit():
                sb += c
        if sb != "":
            b.append(int(sb))
    return s


print(solve(input))

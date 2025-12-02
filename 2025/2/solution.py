# 1.1
file = 'input.txt'
input = [e.split('-') for e in open(file).read().replace('\n', '').split(',')]

def isInvalid(s:str) -> bool:
    if len(s)%2 != 0:
        return False
    n = len(s)//2
    for i in range(n):
        if s[i] != s[n+i]:
            return False
    return True

def solve(input):
    invalids = []
    for (start, end) in input:
        for v in range(int(start), int(end)+1):
            if isInvalid(str(v)):
                invalids.append(v)
    return sum(invalids)

print(solve(input))

# 1.1
file = 'input.txt'
input = [e.split('-') for e in open(file).read().replace('\n', '').split(',')]

def isInvalid(s:str) -> bool:
    n = len(s)
    divisors = [i for i in range(1, n//2+1) if n%i==0]
    return any(isInvalidD(s, d) for d in divisors)

def isInvalidD(s:str, d:int) -> bool:
    n = len(s)
    for i in range(d):
        c = s[i]
        j = d+i
        while j<n:
            if s[j] != c:
                return False
            j += d
    return True

def solve(input):
    invalids = []
    for (start, end) in input:
        for v in range(int(start), int(end)+1):
            if isInvalid(str(v)):
                invalids.append(v)
    return sum(invalids)

print(solve(input))

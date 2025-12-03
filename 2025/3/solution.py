file = 'input.txt'
input = [list(map(int, line)) for line in open(file).read().splitlines()]

def solve(input, digits):
    total = 0
    for l in input:
        l = [(v, i) for i, v in enumerate(l)]
        l.sort(reverse=True, key=lambda x: (x[0], -x[1]))
        n = len(l)
        values = ""
        for d in range(digits-1, -1, -1):
            for (value, index) in l:
                if index < n-d:
                    values += str(value)
                    l = [(v, i) for v, i in l if i>index]
                    break
        total += int(values)
    return total

print(solve(input, 12))




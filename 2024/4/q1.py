def findXmas(a:list, i, j):
    min_l = 3
    max_h = len(a)-4
    max_w = len(a[0])-4
    r = [[" "]*4 for _ in range(8)]
    for k in range(4):
        if i<min_l or j<min_l: break
        r[0][k] = a[i-k][j-k]
    for k in range(4):
        if j<min_l: break
        r[1][k] = a[i][j-k]
    for k in range(4):
        if i>max_h or j<min_l: break
        r[2][k] = a[i+k][j-k]
    for k in range(4):
        if i<min_l: break
        r[3][k] = a[i-k][j]
    for k in range(4):
        if i>max_h: break
        r[4][k] = a[i+k][j]
    for k in range(4):
        if i<min_l or j>max_w: break
        r[5][k] = a[i-k][j+k]
    for k in range(4):
        if j>max_w: break
        r[6][k] = a[i][j+k]
    for k in range(4):
        if i>max_h or j>max_w: break
        r[7][k] = a[i+k][j+k]
    return sum([''.join(s) == "XMAS" for s in r])

a = open("input.txt", "r").read().split('\n')

h = len(a)
w = len(a[0])

print(sum([sum([findXmas(a, j, i) for j in range(w)]) for i in range(h)]))
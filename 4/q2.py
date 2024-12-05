def findXmas(a:list, i, j):
    min_l = 1
    max_h = len(a)-2
    max_w = len(a[0])-2
    r1 = [" "]*3
    r2 = [" "]*3
    for k in range(3):
        if i < min_l or i > max_h or j < min_l or j > max_w: break
        r1[k] = a[i-1+k][j-1+k]
    for k in range(3):
        if i < min_l or i > max_h or j < min_l or j > max_w: break
        r2[k] = a[i-1+k][j+1-k]
    r1 = ''.join(r1)
    r2 = ''.join(r2)
    return (r1 == "SAM" or r1 == "MAS") and (r2 == "SAM" or r2 == "MAS")

a = open("input.txt", "r").read().split('\n')

h = len(a)
w = len(a[0])

print(sum([sum([findXmas(a, j, i) for j in range(w)]) for i in range(h)]))
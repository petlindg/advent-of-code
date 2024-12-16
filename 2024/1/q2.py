import re

def mergeSort(xs:list):
    length = len(xs)
    if length <= 1:
        return xs

    left = xs[0:length//2]
    right = xs[length//2:length]
    left = mergeSort(left)
    right = mergeSort(right)
    
    lenleft = len(left)
    lenright = len(right)

    sorted = []
    i=0
    j=0
    while True:
        if i == lenleft:
            sorted += right[j:lenright]
            break
        elif j == lenright:
            sorted += left[i:lenleft]
            break
        elif left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    return sorted

def distance(l1, l2):
    r = 0
    for (x, y) in zip(l1, l2):
        r += abs(x-y)
    return r

f = open("input.txt", "r").read().split('\n')

l1 = [int(f[i].split("   ")[0]) for i in range(0, len(f))]
l2 = [int(f[i].split("   ")[1]) for i in range(0, len(f))]

def getOcc(e, xs):
    # find start and end index of e
    i = 0
    j = len(xs)-1
    while True:
        p = (i+j)//2
        # print("p:" + str(p) + " xs[p]:" + str(xs[p]) + " i:" + str(i) + " j:" + str(j) + " e:" + str(e))
        if i==j and xs[p] != e:
            return 0
        if xs[p] < e:
            i = p+1
        elif xs[p] > e:
            j = p
        else:
            while xs[i] < e:
                i += 1
            while xs[j] > e:
                j -= 1
            return j-i+1


l1 = mergeSort(l1)
l2 = mergeSort(l2)
# d = distance(l1, l2)
d = sum([i*getOcc(i, l2) for i in l1])


# print(getOcc(5, mergeSort([5,4,3,2,1,5])))

print(d)
def create(nums):
    arr = []
    i = 0
    c = 0
    while i < len(nums):
        if i%2==0:
            for _ in range(nums[i]):
                arr.append(c)
            c+=1
        else:
            for _ in range(nums[i]):
                arr.append('.')
        i+=1
    return arr

def merge(arr):
    rf = []
    i = 0
    while i < len(arr):
        if arr[i]=='.':
            i1 = i
            while arr[i] == '.':
                i+=1
            i2 = i
            rf.append((i1, i2))
        i+=1
    print(rf)
    rn = []
    i = 0
    while i < len(arr):
        if arr[i]!='.':
            e = arr[i]
            i1 = i
            while i<len(arr) and arr[i] == e:
                i+=1
            i2 = i
            rn.append((i1, i2))
        else:
            i+=1
    rn.reverse()
    for (i1, i2) in rn:
        for j in range(len(rf)):
            if j >= len(rf):
                break
            (j1, j2) = rf[j]
            if i2-i1 <= j2-j1 and j1 < i1:
                arr[j1:j1+i2-i1] = arr[i1:i2]
                arr[i1:i2] = ['.']*(i2-i1)
                if j2-j1 != i2-i1:
                    k1=j1+i2-i1
                    k2=k1+(j2-j1)-(i2-i1)
                    rf[j] = (k1, k2)
                    break
                else:
                    rf.remove(rf[j])
                    break
    return arr

def checksum(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i]!='.':
            sum += arr[i]*i
    return sum

nums = list(map(int, open("input.txt", "r").read()))

arr = create(nums)
merged = merge(arr)
sum = checksum(merged)

print(sum)
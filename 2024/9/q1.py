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
    i=0
    j = len(arr)-1
    while arr[j] == '.':
        j-=1
    while i<j:
        if arr[i]=='.':
            arr[i] = arr[j]
            j-=1
            while arr[j] == '.':
                j-=1
        i+=1
    return arr[0:j+1]

def checksum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]*i
    return sum

nums = list(map(int, open("input.txt", "r").read()))

arr = create(nums)
merged = merge(arr)
sum = checksum(merged)

print(sum)
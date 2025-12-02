# 1.1
file = open('input.txt').read()
input = [(e[0], int(e[1:])) for e in file.splitlines()]

value = 50
count = 0
for (d, v) in input:
    if d=='L':
        v = -v
    value = (value+v)%100
    if value == 0:
        count += 1
print(count)

# 1.2
file = open('input.txt').read()
input = [(e[0], int(e[1:])) for e in file.splitlines()]

value = 50
count = 0
for (d, v) in input:
    if d=='L':
        if value == 0:
            distance = 100
        else:
            distance = value
        count += (100+v-distance)//100
        value = (value-v)%100
    if d=='R':
        if value == 0:
            distance = 100
        else:
            distance = (100-value)
        count += (100+v-distance)//100
        value = (value+v)%100
print(count)

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        c = self
        s = ""
        while c != None:
            s += " "
            s += str(c.val)
            c = c.next
        return s
    def __len__(self):
        c = self
        count = 0
        while c != None:
            count += 1
            c = c.next
        return count
    def blink(self):
        c = self
        while c != None:  
            v = c.val
            s = str(v)
            l = len(s)
            if v==0:
                c.val = 1
                c=c.next
            elif l%2==0:
                v1 = int(s[0:l//2])
                v2 = int(s[l//2:l])
                nn = Node(v2, c.next)
                c.val = v1
                c.next = nn
                c = nn.next
            else:
                c.val *= 2024
                c = c.next

def getNodes(l):
    l.reverse()
    n1 = None
    for v in l:
        n = Node(int(v), n1)
        n1 = n
    return n

l = open("input.txt", "r").read().split(' ')
b = 25
n = getNodes(l)
[n.blink() for _ in range(b)]
print(len(n))
n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))
c = [0 for i in range(n+1)]

for i in range(n+1):
    if i==0:
        c[i] = a[0]
    elif i==n:
        c[i] = l-a[i-1]
    else:
        c[i] = a[i] - a[i-1]
def is_possible(m):
    global n,l,k,c

    current = 0
    cuts = 0
    for c_i in c:
        current += c_i
        if current>=m:
            current = 0
            cuts += 1
    if cuts>=k+1:
        return True
    else:
        return False
l=0
r=1000000000
while l!=r:
    m = (l+r)//2
    if m == l:
        break
    if is_possible(m):
        l = m
    else:
        r = m
print(l)
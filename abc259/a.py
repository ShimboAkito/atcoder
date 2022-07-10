n,m,x,t,d = map(int, input().split())

c = n
ans = t

while True:
    c -= 1
    if c<x:
        ans-=d
    else:
        pass
    if c==m:
        break

print(ans)
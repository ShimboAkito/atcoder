n,q= map(int,input().split())
s = input()

ind = 0
for i in range(q):
    t,x = map(int,input().split())
    if t==1:
        ind = (ind-x)%n
    elif t==2:
        print(s[(ind+x-1)%n])


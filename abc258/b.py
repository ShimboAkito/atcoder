from os import nice


n = int(input())
a = [[0 for i in range(n)]for i in range(n)]
for i in range(n):
    b = input()
    for j in range(n):
        a[i][j] = int(b[j])

di=[-1,0,1]
dj=[-1,0,1]
ans= []
M = 0
Mi=[]
Mj=[]
for i in range(n):
    for j in range(n):
        if a[i][j] >M:
            M=a[i][j]

for i in range(n):
    for j in range(n):
        if a[i][j]==M:
            Mi.append(i)
            Mj.append(j)
        
M2 = 0
Di = 0
Dj = 0
ans_can = []
ans_list = []
for mi,mj in zip(Mi,Mj):
    for i in di:
        for j in dj:
            if i==0 and j==0:
                continue
            ans_can=[]
            ni = mi
            nj = mj
            for k in range(n):
                ans_can.append(str(a[ni][nj]))
                ni = (ni+i)%n
                nj = (nj+j)%n
            ans_can_int = int(''.join(ans_can))
            ans_list.append(ans_can_int)


print(max(ans_list))


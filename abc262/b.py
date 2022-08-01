n, m = map(int,input().split())
u = [0 for i in range(m)]

v = [0 for i in range(m)]
D = [[0 for i in range(n)] for i in range(n)]

for i in  range(m):
    u[i], v[i] = map(int,input().split())
    D[u[i]-1][v[i]-1] = 1
    D[v[i]-1][u[i]-1] = 1
count = 0
for a in range(n):
    for b in range(a, n):
        for c in range(b, n):
            if D[a-1][b-1] == 1 and D[b-1][c-1]==1 and D[c-1][a-1] == 1:
                count +=1

print(count)

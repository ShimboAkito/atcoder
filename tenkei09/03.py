import sys
sys.setrecursionlimit(200000)

n = int(input())

A = [0 for i in range(n)]
B = [0 for i in range(n)]

D = [float('inf') for i in range(n)]
roads = [[] for i in range(n)]
visit = [0 for i in range(n)]

def dfs(n):
    global D, visit, roads
    for to in roads[n]:
        if visit[to]==1:
            continue

        if visit[to]==0:
            visit[to]=1
            if D[to]>D[n] + 1:
                D[to] = D[n] + 1
                dfs(to)



for i in range(n-1):
    A[i], B[i] = map(int, input().split())
    roads[A[i]-1].append(B[i] - 1)
    roads[B[i]-1].append(A[i] - 1)
    


D[0] = 0
visit[0]= 1
dfs(0)

s = D.index(max(D))
visit[s]=1
D = [float('inf') for i in range(n)]
D[s] = 0
visit = [0 for i in range(n)]
dfs(s)
print(max(D)+1)
n, k, q =map(int,input().split())
p = [False for i in range(n)]

A = list(map(int, input().split()))
L = list(map(int, input().split()))

for a in A:
    p[a-1] = True

for l in L:
    if A[l-1]==n:
        continue
    elif l==k:
        A[l-1]+= 1
    elif A[l]-A[l-1] == 1:
        continue
    else:
        A[l-1] += 1

print(" ".join([str(i) for i in A]))
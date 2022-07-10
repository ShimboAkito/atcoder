H, W = map(int,input().split())
A = []
B = [[0 for i in range(W)] for i in range(H)]

rows = [0 for i in range(H)]
cols = [0 for i in range(W)]

for i in range(H):
    A.append(list(map(int, input().split())))

for i in range(H):
    for j in range(W):
        rows[i] += A[i][j]
        cols[j] += A[i][j]

for i in range(H):
    for j in range(W):
        B[i][j] = rows[i] + cols[j] - A[i][j]
        B[i][j] = str(B[i][j])

for i in range(H):
    print(' '.join(B[i]))
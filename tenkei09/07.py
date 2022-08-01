n = int(input())
A = list(map(int, input().split()))
q= int(input())
B = []

C = [None for i in range(q)]
S = []
current = 0
ans = 0
for i in range(q):
    B.append([i,int(input())])
A = list(set(A))
A = sorted(A)
B = sorted(B, key = lambda x: x[1])
print(A,B)

for i in range(q):
    b = B[i][1]
    a = A[current]
    a_next = A[current+1]
    d = abs(b-a)
    d_next = abs(b-a_next)

    if d<=d_next:
        C[i] = current
        B[i].append(d)
    else:
        C[i] = current+1
        B[i].append(d_next)
        current =  min(len(A)-1, current+1)

B = sorted(B, key = lambda x: x[0])
print(B)
for b in B:
    print(b[2])
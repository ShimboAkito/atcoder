n = int(input())
a = list(map(int, input().split()))
e = 0
d = 0
ans = 0
for i in range(n):
    if a[i] == i+1:
        e += 1
    elif a[a[i]-1] == i+1:
        d +=1
ans += (e*(e-1))//2
ans += d//2
print(ans)
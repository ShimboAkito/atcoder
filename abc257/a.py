n, x= map(int,input().split())
l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = ''
for i in range(26):
    s += l[i] * n

print(s[x-1])
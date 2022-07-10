from collections import defaultdict
import math 
n = int(input())
sx,sy,tx,ty = map(int,input().split())
sn,tn = 0,0
D = [[0 for i in range(n)]for i in range(n)]


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def is_in(x, y, cx, cy, r):
    dx = cx-x
    dy = cy-y
    d = abs(dx**2+dy**2-r**2)

    if d == 0:
        return True
    else:
        return False
def is_cross(ax, ay, ar, bx, by, br):
    dx = ax - bx
    dy = ay-by
    d = dx**2 + dy**2
    if d<=(ar+br)**2 and d>=(ar-br)**2:
        return True
    else:
        return False

x = [0 for i in range(n)]
y = [0 for i in range(n)]
r = [0 for i in range(n)]
for i in range(n):
    x[i], y[i], r[i] = map(int,input().split())

for i in range(n):
    if is_in(sx,sy, x[i],y[i],r[i]):
        sn = i
    if is_in(tx,ty, x[i],y[i],r[i]):
        tn = i
    for j in range(n):
        if is_cross(x[i],y[i], r[i],x[j],y[j],r[j]):
            D[i][j]=1

uf = UnionFind(n)
for i in range(n):
    for j in range(n):
        if D[i][j]==1:
            uf.union(i,j)

if uf.find(sn)==uf.find(tn):
    print('Yes')
else:
    print('No')
import cmath

import math
pi = math.pi
a,b,d =map(int,input().split())

e = cmath.rect(1, (d/180)*pi)
z = complex(a,b)

ans = z*e

print(ans.real, ans.imag)
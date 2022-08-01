y = int(input())
ans = y%4

if ans == 0:
    print(y+2)
elif ans == 1:
    print(y+1)
elif ans == 2:
    print(y)
elif ans == 3:
    print(y + 3)
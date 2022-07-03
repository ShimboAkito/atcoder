n, x = map(int,input().split())

time_list = []

abtime_list = []

A = [0 for i in range(n)]
B = [0 for i in range(n)]
for i in range(n):
    A[i], B[i] = map(int, input().split())

for i in range(n):
    if i==0:
        abtime_list.append(0)
    else:
        abtime_list.append(abtime_list[i-1]+A[i-1]+B[i-1])
    time_list.append(abtime_list[i]+B[i]*abs((x-i))+A[i])
print(min(time_list))
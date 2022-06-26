n = int(input())
s = input()
w = list(map(int, input().split()))

p = []
for i in range(n):
    p.append((w[i], s[i]))

p = sorted(p, key=lambda x: x[0], reverse=True)
p2 = sorted(p, key=lambda x: x[0])
ruiseki = [0 for i in range(n+1)]
ruiseki2 = [0 for i in range(n+1)]
for i, person in enumerate(p):
    if person[1] == "1":
        ruiseki[i+1] = ruiseki[i]+1
    else:
        ruiseki[i+1] =ruiseki[i]-1

for i, person in enumerate(p2):
    if person[1] == "0":
        ruiseki2[i+1] = ruiseki2[i]+1
    else:
        ruiseki2[i+1] =ruiseki2[i]-1



th = p[ruiseki.index(max(ruiseki))-1][0]
th2 = p2[ruiseki2.index(max(ruiseki2))-1][0]
th3 = th+0.5
th4 = th2-0.5
ans = 0
ans2= 0
ans3 =0
ans4=0
for person in p:
    if (person[0]>=th and person[1]=="1") or (person[0]<th and person[1]=='0'):
        ans += 1
    if (person[0]>=th3 and person[1]=="1") or (person[0]<th3 and person[1]=='0'):
        ans3 += 1
for person in p2:
    if (person[0]>th2 and person[1]=="1") or (person[0]<=th2 and person[1]=='0'):
        ans2 += 1
    if (person[0]>th4 and person[1]=="1") or (person[0]<=th4 and person[1]=='0'):
        ans4 += 1
                
flag=True
for st in s:
    if st=='0':
        continue
    else:
        flag= False
        break
if flag:
    print(n)
else:
    print(max(ans,ans2,ans3, ans4))
n = int(input())
s = input()
w = list(map(int, input().split()))

p = []
for i in range(n):
    p.append((w[i], s[i]))

p = sorted(p, key=lambda x: x[0], reverse=True)
p2 = sorted(p, key=lambda x: x[0])
ruiseki = [0 for i in range(n+1)]
ruiseki2 = [0 for i in range(n+1)]
for i, person in enumerate(p):
    if person[1] == "1":
        ruiseki[i+1] = ruiseki[i]+1
    else:
        ruiseki[i+1] =ruiseki[i]-1

for i, person in enumerate(p2):
    if person[1] == "0":
        ruiseki2[i+1] = ruiseki2[i]+1
    else:
        ruiseki2[i+1] =ruiseki2[i]-1



th = p[ruiseki.index(max(ruiseki))-1][0]
th2 = p2[ruiseki2.index(max(ruiseki2))-1][0]
th3 = th+0.5
th4 = th2-0.5
ans = 0
ans2= 0
ans3 =0
ans4=0
for person in p:
    if (person[0]>=th and person[1]=="1") or (person[0]<th and person[1]=='0'):
        ans += 1
    if (person[0]>=th3 and person[1]=="1") or (person[0]<th3 and person[1]=='0'):
        ans3 += 1
for person in p2:
    if (person[0]>th2 and person[1]=="1") or (person[0]<=th2 and person[1]=='0'):
        ans2 += 1
    if (person[0]>th4 and person[1]=="1") or (person[0]<=th4 and person[1]=='0'):
        ans4 += 1
                
flag=True
for st in s:
    if st=='0':
        continue
    else:
        flag= False
        break
if flag:
    print(n)
else:
    print(max(ans,ans2,ans3, ans4))

import difflib
from stat import S_IFDIR


S = input()
T = input()

def make_pair_list(S):
    diff_list = []
    ret_list = []
    for i in range(len(S)-1):
        if S[i+1]!=S[i]:
            diff_list.append(i+1)
    if len(diff_list)!=0:
        ret_list.append((S[0], diff_list[0]))
        for i in range(len(diff_list)-1):
            ret_list.append((S[diff_list[i]], diff_list[i+1]-diff_list[i]))
        ret_list.append((S[diff_list[-1]], len(S)-diff_list[-1]))
    else:
        ret_list.append((S[0], len(S)))
    return ret_list
Sd= make_pair_list(S)
Td= make_pair_list(T)

ans = True

if len(Sd)!=len(Td):
    ans = False
else:
    for s, t in zip(Sd, Td):
        if s[0]!=t[0]:
            ans = False
            break
        elif s[1]>t[1]:
            ans =False
            break
        elif s[1]<t[1] and s[1]<2:
            ans =False
            break

if ans:
    print('Yes')
else:
    print('No')


n = input()

def check(s):
    c = 0
    for l in s:
        if c < 0:
            return False
        if l=='0':
            c+=1
        elif l=='1':
            c-=1
        else:
            print('error')
    if c == 0:
        return True
    else:
        return False
def print_s(s):
    for l in s:
        if l=='0':
            print('(', end='')
        else:
            print(')', end='')
    print()
        

for i in range(2**int(n)):
    s = format(i, '0'+n+'b')
    if check(s):
        print_s(s)


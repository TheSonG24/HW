def f(p):
    s = ''
    while p != 0:
        s += str(p % 2)
        p = p // 2
    return s[:: -1]


for n in range(11, 20):
    k = n
    n = f(n)
    if int(n) % 2 == 0:
        r = '1' + n + '00'
        if int(r, 2) > 190:
            print(r, k)
            break
    else:
        r = n + f(n.count('1'))
        if int(r, 2) > 190:
            print(r, k)
            break

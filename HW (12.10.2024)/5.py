def f(p):
    s = ''
    while p != 0:
        s += str(p % 3)
        p = p // 3
    return s[:: -1]


e = []
for n in range(1, 10000):
    n = f(n)
    n = n.replace('1', 'a')
    n = n.replace('2', 'b')
    n = n.replace('0', 'c')
    n = n.replace('a', '2')
    n = n.replace('b', '0')
    n = n.replace('c', '1')
    n = int(n)
    pp = str(n)
    if n != 0:
        R = pp[:: -1] + f(pp.count('1')+pp.count('2')*2)
        if int(R, 3) > 10 ** 4:
            e.append(int(R, 3))
print(min(e))

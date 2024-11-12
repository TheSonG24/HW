def f(p):
    s = ''
    while p != 0:
        s += str(p % 3)
        p = p // 3
    return s[:: -1]


for n in range(50):
    k = n
    n = f(n)
    tvo = f(n.count('2'))
    n = n + tvo
    odin = f(n.count('1'))
    n = n + odin
    nol = str(f(n.count('0')))
    if nol == '':
        nol = '0'
    R = int(n + nol, 3)
    if R < 1000:
        print(R, n, k)

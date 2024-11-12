def f(p):
    s = ''
    while p != 0:
        s += str(p % 5)
        p = p // 5
    return s[:: -1]


for n in range(11, 300):
    k = n
    n = f(n)
    if k % 5 == 0:
        if len(n) > 2:
            R = n + n[-3:]
            if int(R, 5) > 375:
                print(R, k)
                break
    else:
        ostatok = f(k % 5 * 5)
        R = ostatok + n
        if int(R, 5) > 375:
            print(R, k)
            break

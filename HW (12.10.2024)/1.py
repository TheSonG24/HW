def f(p):
    s = ''
    while p != 0:
        s += str(p % 3)
        p = p // 3
    return s[:: -1]


# я тут случайно начал 2 делать, в 1 легко)) а переделывать леньь
n = f(int(input()))
tvo = f(n.count('2'))
n = n + tvo
tree = f(n.count('1'))
n = n + tree
nol = str(f(n.count('0')))
if nol == '':
    nol = '0'
print(int(n + nol, 3))


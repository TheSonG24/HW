import itertools as f

k = list(f.product('abcx', repeat=5))
t = 0
for x in k:
    x = ''.join(x)
    if x.count('x') == 1 and (x[0] == 'x' or x[4] == 'x'):
        t += 1
print(t)


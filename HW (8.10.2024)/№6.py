import itertools as f

t = list(f.product('123456', repeat=10))
sogl = ['3', '4', '5', '6']
i = 0
o = 0
for x in t:
    x = ''.join(x)
    i += 1
    if i % 3 == 0 and x[0] in sogl and x.count('5') == 1:
        o += 1
print(o)

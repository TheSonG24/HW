import itertools as f

t = list(f.product('авеилря', repeat=3))
i = 0
for x in t:
    x = ''.join(x)
    i += 1
    if x.count('в') == 1 and x.count('а') == 0:
        print(i)
        break

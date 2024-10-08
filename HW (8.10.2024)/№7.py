import itertools as f

t = list(f.product('екмопрть', repeat=5))
i = 0
o = 0
for x in t:
    x = ''.join(x)
    i += 1
    if x.count('к') == 0 and x.count('р') == 2:
        o = i
print(o)

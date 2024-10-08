import itertools as f

t = list(f.product('мангуст', repeat=6))
i = 0
for x in t:
    x = ''.join(x)
    if x[0] != 'а' and x.count('у') >= 1 and x.count('м') == 2:
        i += 1
print(i)

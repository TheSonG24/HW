import itertools as f

k = (f.product('012345678', repeat=5))
summ = 0
dat = ['1', '3', '7']

for x in k:
    p = ''.join(x)
    if p[0] != '0' and p.count('5') == 1:
        index_5 = p.index('5')

        if index_5 > 0 and p[index_5 - 1] in dat:
            continue
        if index_5 < 4 and p[index_5 + 1] in dat:
            continue

        summ += 1

print(summ)
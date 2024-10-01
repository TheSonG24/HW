import itertools as f
k = list(f.product('векно', repeat=5))
summ = 0
for x in k:
    x = ''.join(x)
    summ += 1
    if x[0] == 'о':
        print(summ)
        break

import itertools as f

k = list(f.product('ежи', repeat=5))
summ = 0
for x in k:
    x = ''.join(x)
    summ += 1
    if summ == 238:
        print(x)
        break

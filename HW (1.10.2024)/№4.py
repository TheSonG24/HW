import itertools as f
k = list(f.product('апрсу', repeat=4))
summ = 0
for x in k:
    x = ''.join(x)
    summ += 1
    if x.count('а') == 0:
        print(summ)
        break


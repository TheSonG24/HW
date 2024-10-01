import itertools as f
k = list(f.product('abcdex', repeat=4))
summ = 0
for x in k:
    x = ''.join(x)
    if x.count('x') == 1:
        summ += 1
print(summ)
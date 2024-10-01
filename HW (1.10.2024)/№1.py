import itertools as f
k = list(f.product('пятница', repeat=5))
summ = 0
for x in k:
    x = ''.join(x)
    if x[0] != 'н' and x.count('я') == 1:
        summ += 1
print(summ)
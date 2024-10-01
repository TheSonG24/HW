import itertools as f
k = list(f.product('метро', repeat=4))
sogl = ['м', 'т', 'р']
gl = ['е', 'о']
summ = 0
for x in k:
    x = ''.join(x)
    if x[0] in sogl and x[3] in gl:
        print(x)
        summ += 1
print(summ)

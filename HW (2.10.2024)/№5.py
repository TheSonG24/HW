import itertools as f
k = list(f.product('полина', repeat=8))
summ = 0
for x in k:
    x = ''.join(x)
    if (x.count('о') + x.count('и') + x.count('а')) > (x.count('п') + x.count('л') + x.count('н')):
        summ += 1
print(summ)

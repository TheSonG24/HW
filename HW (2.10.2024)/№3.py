import itertools as f
k = list(f.product('0123456', repeat=4))
summ = 0
for x in k:
    x = ''.join(x)
    if x[0] < x[1] < x[2] < x[3]:
        summ+=1
print(summ)

import itertools as f

k = list(f.permutations('01234567', r=5))
dat1 = ['0', '2', '4', '6']
dat2 = ['3', '5', '7']
summ = 0
for x in k:
    x = ''.join(x)
    if x[0] != '0' and x.count('1') == 0 and ((x[0] in dat1 and x[1] in dat2 and x[2] in dat1 and x[3] in dat2 and x[4] in dat1) \
            or (x[0] in dat2 and x[1] in dat1 and x[2] in dat2 and x[3] in dat1 and x[4] in dat2)):
        summ += 1
print(summ)

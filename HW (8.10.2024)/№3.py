import itertools as f

t = list(f.permutations('0123456789', r=6))
dat1 = ['1', '3', '5', '7', '9']
dat2 = ['0', '2', '4', '6', '8']
i = 0
for x in t:
    x = ''.join(x)
    if (x[0] != '0') and \
            ((x[0] in dat1 and x[1] in dat2 and x[2] in dat1 and x[3] in dat2 and x[4] in dat1 and x[5] == '0') or \
             (x[0] in dat2 and x[1] in dat1 and x[2] in dat2 and x[3] in dat1 and x[4] in dat2 and x[5] == '5')):
        i += 1
print(i)

import itertools as f
k = list(f.product('ярослав', repeat=5))
summ = 0
for x in k:
    x = ''.join(x)
    if x.count('я') <= 1 and x.count('р') <= 1 and x.count('о') <= 1 and \
            x.count('с') <= 1 and x.count('л') <= 1 and x.count('а') <= 1 and x.count('в') <= 1 and \
            x[0] != 'я' and x[0] != 'о' and x[0] != 'а' and \
            x[1] != 'р' and x[1] != 'с' and x[1] != 'л' and x[1] != 'в' and \
            x[2] != 'я' and x[2] != 'о' and x[2] != 'а' and \
            x[3] != 'р' and x[3] != 'с' and x[3] != 'л' and x[3] != 'в' and\
            x[4] != 'я' and x[4] != 'о' and x[4] != 'а':
        summ += 1
print(summ)

import itertools as f

k = list(f.product('аоу', repeat=6))
t = 0
for x in k:
    x = ''.join(x)
    t += 1
    if x == 'оуууоо':
        print(t)
        break

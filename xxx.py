l1 = [1, 2, 3, 5]
l2 = [1, 2, 3]
l3 = []

for i in l1:
    for y in l2:
        if i == y:
            l3.append(i)

if len(l3) == 3:
    print('gg')
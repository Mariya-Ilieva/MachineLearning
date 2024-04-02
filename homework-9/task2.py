l = [1, 2, 3]
gen = (l[i] for i in range(len(l) - 1, -1, -1))

for i in gen:
    print(i)

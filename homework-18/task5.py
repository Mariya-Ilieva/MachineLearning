def y_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0

    temp = start

    while (step > 0 and temp < end) or (step < 0 and temp > end):
        yield temp

        temp += step

# for x in y_range(2, 22, 2):
#     print(x)

for x in y_range(11):
    print(x)

# for x in y_range(5, 0, -1):
#     print(x)

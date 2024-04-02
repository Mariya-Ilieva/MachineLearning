def cut(data, bins, labels=None, right=True):
    categories = []

    for d in data:
        for i in range(len(bins)):
            if i == 0:
                if (not right and d < bins[i]) or (right and d <= bins[i]):
                    categories.append(labels[i] if labels and i < len(labels) else i)
                    break
            elif i == len(bins) - 1:
                categories.append(labels[i] if labels and i < len(labels) else i)
                break
            else:
                if bins[i] < d <= bins[i + 1]:
                    categories.append(labels[i] if labels and i < len(labels) else i)
                    break

    return categories

def qcut(data, q, labels=None):
    sorted_data = sorted(data)
    quantiles = [sorted_data[int(len(sorted_data) * quantile)] for quantile in q]
    categories = []

    for d in data:
        for i in range(len(quantiles)):
            if i == 0:
                if d <= quantiles[i]:
                    categories.append(labels[i] if labels and i < len(labels) else i)
                    break
            elif i == len(quantiles) - 1:
                categories.append(labels[i] if labels and i < len(labels) else i)
                break
            else:
                if quantiles[i] < d <= quantiles[i + 1]:
                    categories.append(labels[i] if labels and i < len(labels) else i)
                    break

    return categories

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']

print(cut(ages, bins))
print(cut(ages, bins, right=False))
print(cut(ages, bins, labels=group_names))

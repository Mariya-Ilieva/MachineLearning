class Categorical:
    def __init__(self, codes, categories=None, ordered=False):
        self._codes = codes

        if categories is None:
            self._categories = list(set(codes))
        else:
            self._categories = categories

        self._ordered = ordered

    @classmethod
    def from_codes(cls, codes, categories=None, ordered=False):
        return cls(codes, categories, ordered)

    @property
    def cat(self):
        return self._categories

    @property
    def codes(self):
        return self._codes

    def value_counts(self):
        counts = {}

        for code in self._codes:
            counts[code] = counts.get(code, 0) + 1

        return counts

    def add_categories(self, new_categories):
        self._categories.extend(new_categories)

    def as_ordered(self):
        self._ordered = True

    def as_unordered(self):
        self._ordered = False

    def remove_categories(self, categories):
        self._categories = [cat for cat in self._categories if cat not in categories]
        self._codes = [code if code in self._categories else None for code in self._codes]

    def remove_unused_categories(self):
        used_categories = set(self._codes)
        self._categories = [cat for cat in self._categories if cat in used_categories]

    def rename_categories(self, new_categories):
        self._categories = new_categories
        new_indices = {cat: idx for idx, cat in enumerate(new_categories)}
        self._codes = [new_indices[cat] if cat in new_categories else None for cat in self._codes]

    def reorder_categories(self, new_categories, ordered=False):
        self.rename_categories(new_categories)

        if ordered:
            self.as_ordered()

    def set_categories(self, new_categories, ordered=False):
        if ordered:
            self.as_ordered()
        else:
            self.as_unordered()

        self._categories = new_categories
        new_indices = {cat: idx for idx, cat in enumerate(new_categories)}
        self._codes = [new_indices[cat] if cat in new_categories else None for cat in self._codes]

    def astype(self, dtype):
        if dtype == 'category':
            return Categorical(categories=self.cat, codes=self.codes)
        else:
            raise ValueError('Unsupported dtype for conversion to Categorical.')

    def __repr__(self):
        return f'Categorical(categories={self.cat}, codes={self.codes})'


codes = [0, 1, 0, 1, 2]
categories = ['a', 'b', 'c']
cat = Categorical(codes, categories)

print(cat.value_counts())
cat.add_categories(['d'])
print(cat.cat)
cat.as_ordered()
print(cat.codes)
cat.remove_categories(['d'])
print(cat.cat)
cat.remove_unused_categories()
print(cat.cat)
cat.rename_categories(['x', 'y', 'z'])
print(cat.cat)
cat.reorder_categories(['z', 'x', 'y'], ordered=True)
print(cat.cat)
cat.set_categories(['m', 'n', 'o'], ordered=False)
print(cat.cat)

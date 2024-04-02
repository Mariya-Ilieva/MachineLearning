import numpy as np


class Categorical:
    def __init__(self, codes, categories=None, ordered=False):
        self._codes = np.array(codes)

        if categories is None:
            self._categories = np.unique(self._codes)
        else:
            self._categories = np.array(categories)

        self._ordered = ordered

    @classmethod
    def from_codes(cls, codes, categories=None, ordered=False):
        return cls(codes, categories, ordered)

    @property
    def cat(self):
        return self._categories.tolist()

    @property
    def codes(self):
        return self._codes.tolist()

    def value_counts(self):
        unique, counts = np.unique(self._codes, return_counts=True)
        return dict(zip(unique, counts))

    def add_categories(self, new_categories):
        self._categories = np.concatenate((self._categories, new_categories))

    def as_ordered(self):
        self._ordered = True

    def as_unordered(self):
        self._ordered = False

    def remove_categories(self, categories):
        mask = np.isin(self._categories, categories, invert=True)
        self._categories = self._categories[mask]
        self._codes = np.where(np.isin(self._codes, categories), None, self._codes)

    def remove_unused_categories(self):
        mask = np.isin(self._categories, self._codes)
        self._categories = self._categories[mask]

    def rename_categories(self, new_categories):
        self._categories = np.array(new_categories)
        code_mapping = {old_cat: new_cat for old_cat, new_cat in zip(self._categories, new_categories)}
        self._codes = np.array([code_mapping.get(code, None) for code in self._codes])

    def reorder_categories(self, new_categories, ordered=False):
        self.rename_categories(new_categories)
        if ordered:
            self.as_ordered()

    def set_categories(self, new_categories, ordered=False):
        self._categories = np.array(new_categories)
        if ordered:
            self.as_ordered()
        else:
            self.as_unordered()
        code_mapping = {old_cat: new_cat for old_cat, new_cat in zip(self._categories, new_categories)}
        self._codes = np.array([code_mapping.get(code, None) for code in self._codes])

    def astype(self, new_dtype):
        if new_dtype == 'category':
            return self
        elif new_dtype == 'object':
            return np.array([self._categories[code] if code is not None else None for code in self._codes])
        else:
            raise ValueError('Invalid dtype. Allowed values are "category" and "object".')


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

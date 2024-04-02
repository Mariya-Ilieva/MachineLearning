import numpy as np


class Index:
    def __init__(self, data=None, name=None, copy=False):
        self.data = np.array(data) if data is not None else np.array([])
        self._name = name
        self.sorted_indices = sorted(range(len(self.data)), key=lambda x: self.data[x])  # Could be np.argsort(self.data)

        if copy:
            self.data = self.data.copy()

    @property
    def dtype(self):
        return type(self.data[0]) if len(self.data) > 0 else None

    @property
    def name(self):
        return self._name

    @property
    def values(self):
        return self.data

    def _binary_search(self, value):
        low, high = 0, len(self.data)

        while low < high:
            mid = (low + high) // 2

            if self.data[mid] < value:
                low = mid + 1
            else:
                high = mid

        return low

    def _find_indices(self, values):
        indices = []

        for v in values:
            idx = self._binary_search(v)

            if idx < len(self.data) and self.data[idx] == v:
                indices.append(self.sorted_indices[idx])
            else:
                raise ValueError(f'{v} is not in index')

        return indices

    def index(self, value):
        if isinstance(value, (list, tuple)):
            return self._find_indices(value)
        else:
            idx = self._binary_search(value)

            if idx < len(self.data) and self.data[idx] == value:
                return self.sorted_indices[idx]
            else:
                raise ValueError(f'{value} is not in index')

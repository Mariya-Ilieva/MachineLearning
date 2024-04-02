class MultiIndex:
    def __init__(self, levels, codes):
        self.levels = levels
        self.codes = codes

    def __contains__(self, el):
        return el in self.levels

    def index(self, idx):
        if idx not in self.levels:
            raise KeyError(f'Key "{idx}" not found in MultiIndex.')

        return self.levels.index(idx)

    def __getitem__(self, el):
        if isinstance(el, int):
            return self.levels[el]
        elif isinstance(el, slice):
            return self.levels[el.start:el.stop:el.step]
        elif isinstance(el, tuple):
            level_index = self.index(el[0])

            if len(el) == 1:
                return self.codes[level_index]
            else:
                level_codes = self.codes[level_index]
                return [level_codes[i] for i in el[1]]
        else:
            level_index = self.index(el)
            return self.codes[level_index]

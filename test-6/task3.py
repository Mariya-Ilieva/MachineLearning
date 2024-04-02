class Counter(dict):
    def __init__(self, itr, *args, **kwargs):
        super(Counter, self).__init__()
        self.update(itr, **kwargs)

    def update(self, itr, **kwargs):
        if not hasattr(itr, '__iter__'):
            raise TypeError(f'Invalid iterable type for {itr}')

        if hasattr(itr, 'items'):
            for k, v in itr.items():
                self[k] = self.get(k, 0) + v
        else:
            for el in itr:
                self[el] = self.get(el, 0) + 1

    def most_common(self, n):
        res = []

        for i in range(n):
            m = max(self.items(), key=lambda x: x[1])
            res.append(m)
            del self[m[0]]

        self.update(res)
        return res

        # items = sorted(self.items(), key=lambda x: x[1], reverse=True)
        #
        # c = 0
        # for i in items:
        #     yield i
        #     c += 1
        #     if c == n:
        #         break


s = 'hello world'
c = Counter(s)

for e, count in c.most_common(3):
    print(e, '->', count)

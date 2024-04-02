class NumSet:
    def __init__(self, n):
        if not isinstance(n, int):
            raise TypeError('Please provide a valid integer')

        if n < 0:
            raise ValueError(f'Expected a positive value for {n}')

        self.n = n
        self.bitmask = 0

    def add(self, num):
        if 0 <= num <= self.n:
            self.bitmask |= 1 << num
        else:
            raise ValueError(f'Number {num} is out of range (0 to {self.n}).')

    def remove(self, num):
        if 0 <= num <= self.n:
            self.bitmask &= ~(1 << num)
        else:
            raise ValueError(f'Number {num} is out of range (0 to {self.n}).')

    def __contains__(self, num):
        if 0 <= num <= self.n:
            return (self.bitmask & (1 << num)) != 0

        return False

    def __str__(self):
        return str([num for num in range(self.n + 1) if num in self])


ns = NumSet(n=1024)
ns.add(1000)

if 1000 in ns:
    print('found')

ns.add(1500)

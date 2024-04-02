class Average:
    def __init__(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError(f'Invalid value {n} for parameter, must be an integer greater than zero.')

        self.n = n
        self.numbers = []

    def next(self, num):
        self.numbers.append(num)

        idx = max(0, len(self.numbers) - self.n)
        result = self.numbers[idx:]

        return sum(result) / len(result)


avg = Average(3)
print(avg.next(1))
print(avg.next(2))
print(avg.next(3))
print(avg.next(4))
print(avg.next(5))
print(avg.next(0))

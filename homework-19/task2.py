class Average:
    def __init__(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError(f'Invalid value {n} for parameter, must be an integer greater than zero.')

        self.n = n
        self.nums = [0] * n
        self.index = 0

    def next(self, num):
        self.nums[self.index] = num
        self.index = (self.index + 1) % self.n

        if len(self.nums) < self.n:
            yield num
        else:
            average = sum(self.nums) / self.n
            yield average


avg = Average(3)

val = next(avg.next(1))
print(val)
val = next(avg.next(2))
print(val)
val = next(avg.next(3))
print(val)
val = next(avg.next(4))
print(val)
val = next(avg.next(5))
print(val)
val = next(avg.next(0))
print(val)

class NumSet:
    def __init__(self, n):
        self.n = n
        self.elements = [0] * ((n + 1) // 64 + 1)

    def add(self, num):
        if 0 <= num <= self.n:
            self.elements[num // 64] |= 1 << (num % 64)

    def remove(self, num):
        if 0 <= num <= self.n:
            self.elements[num // 64] &= ~(1 << num % 64)

    def __contains__(self, num):
        if 0 <= num <= self.n:
            return (self.elements[num // 64] & (1 << num % 64)) != 0

        return False

    def __str__(self):
        return str([num for num in range(self.n + 1) if num in self])


n = 64
num_set = NumSet(32)
num_set.add(5)
num_set.add(5)
num_set.add(10)

print(num_set)
print(5 in num_set)
print(7 in num_set)

num_set.remove(5)
print(num_set)

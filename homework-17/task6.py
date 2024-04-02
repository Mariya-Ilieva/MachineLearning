from array import array


class NumberSet:
    def __init__(self):
        self.elements = array('b', [0 for _ in range(101)])

    def add(self, num):
        if 0 <= num <= 100:
            self.elements[num] = 1

    def remove(self, num):
        if 0 <= num <= 100:
            self.elements[num] = 0

    def __contains__(self, num):
        if 0 <= num <= 100:
            return self.elements[num]

        return False

    def __str__(self):
        return str([num for num, present in enumerate(self.elements) if present])


num_set = NumberSet()
num_set.add(5)
num_set.add(5)
num_set.add(10)

print(num_set)
print(5 in num_set)
print(7 in num_set)

num_set.remove(5)
print(num_set)

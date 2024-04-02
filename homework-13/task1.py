# def fib(count):
#     fib_nums = [0, 1]
#
#     for _ in range(2, count):
#         fib_nums.append(fib_nums[-1] + fib_nums[-2])
#
#     return fib_nums
#
# for n in fib(22):
#   print(n)


class Fibonacci:
    def __init__(self, count):
        self.count = count
        self.temp = 0
        self.next = 1
        self.c = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.c >= self.count:
            raise StopIteration

        result = self.temp
        self.temp = self.next
        self.next += result
        self.c += 1

        return result


def fib(count):
    return Fibonacci(count)

for n in Fibonacci(10):
    print(n)

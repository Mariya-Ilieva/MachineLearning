# def my_range(start, stop, step):
#     result = []
#     temp = start
#
#     while temp < stop:
#         result.append(temp)
#         temp += step
#
#     return result
#
# for i in my_range(2, 16, 4):
#     print(i)


class MyRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.temp = start

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.temp < self.stop) or (self.step < 0 and self.temp > self.stop):
            result = self.temp
            self.temp += self.step
            return result
        else:
            raise StopIteration


for i in MyRange(2, 32, 4):
    print(i)

# def mergeRanges(intervals):
#     if not intervals:
#         return []
#
#     intervals.sort(key=lambda x: x[0])
#     result = [intervals[0]]
#
#     for start, end in intervals[1:]:
#         last_start, last_end = result[-1]
#
#         if start <= last_end:
#             result[-1] = (last_start, max(last_end, end))
#         else:
#             result.append((start, end))
#
#     return result


class Range:
    def __init__(self, ints, step=1):
        self.start, self.end = ints
        self.step = step

    def contains(self, n):
        return self.start <= n <= self.end

    def overlaps(self, r):
        return self.start <= r.end and r.start <= self.end

    def merge(self, r):
        if self.overlaps(r):
            self.start = min(self.start, r.start)
            self.end = max(self.end, r.end)
            return True
        else:
            return False

    def __str__(self):
        return f'[{self.start}, {self.end}]'

def mergeRanges(intervals):
    if not intervals:
        return []

    ranges = [Range(rang) for rang in intervals]
    ranges.sort(key=lambda x: x.start)
    last = ranges[0]
    result = [last]

    for i in range(1, len(ranges)):
        r = ranges[i]
        if not last.merge(r):
            result.append(r)
            last = r

    output = [[r.start, r.end] for r in result]
    return output


print(mergeRanges([[1, 5], [2, 4]]))
print(mergeRanges([[1, 5], [6, 8]]))
print(mergeRanges([[1, 5], [5, 6]]))
print(mergeRanges([[1, 5], [4, 7], [6, 8]]))

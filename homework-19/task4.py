def custom_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

class Employee:
    def __init__(self, name):
        self.name = name

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return f'{self.name}'


e1 = Employee('Stoyan')
e2 = Employee('Ivan')
e3 = Employee('Petar')
e4 = Employee('Albena')

ea = [e1, e2, e3, e4]
custom_sort(ea)
print(ea)

arr = [3, 5, 1, 4, 0]
custom_sort(arr)
print(arr)

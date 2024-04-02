from dataclasses import dataclass


def max(arr, compare=None):
    if not arr or not isinstance(arr, list):
        raise Exception('Please provide a valid array')

    max_el = arr[0]

    if compare:
        for el in arr:
            if compare(el, max_el):
                max_el = el
    else:
        for el in arr:
            if el > max_el:
                max_el = el

    return max_el

@dataclass
class Employee:
  name: str
  age: int

people = [
  Employee('Ivan', 25),
  Employee('Niki', 33),
  Employee('Desi', 12)
]

oldest = max(people, lambda p1, p2: p1.age > p2.age)
print(oldest)

youngest = max(people, lambda p1, p2: p1.age < p2.age)
print(youngest)

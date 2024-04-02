def deepcopy(obj):
    def deepcopy_class_instance(original, clone):
        for key in original.__dict__:
            setattr(clone, key, deepcopy(getattr(original, key)))

    stack = [(obj, None)]
    cloned = {}

    while stack:
        current, clone = stack.pop()

        if id(current) in cloned:
            continue

        if isinstance(current, (list, tuple)):
            cloned[current] = [None] * len(current)
            stack.extend((current[i], cloned[current]) for i in range(len(current) - 1, -1, -1))
        elif isinstance(current, dict):
            cloned[current] = {}
            stack.extend((key, cloned[current]) for key in current.keys())
        elif hasattr(current, '__dict__'):
            cloned[current] = type(current).__new__(type(current))
            deepcopy_class_instance(current, cloned[current])
        else:
            cloned[current] = current

    return cloned[obj]


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Manager:
    def __init__(self, name):
        self.name = name


class Intern:
    def __init__(self, name):
        self.name = name


a = [Employee('Ivan', age=24), Manager('Georgi'), [1, 2, 3], Intern('Stoyan'), 'Hello']
b = deepcopy(a)

for original, copied in zip(a, b):
    if hasattr(original, '__dict__'):
        print(original.__dict__, 'vs', copied.__dict__)
    else:
        print(original, 'vs', copied)

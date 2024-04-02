def deepcopy(obj):
    cloned = {}

    if id(obj) in cloned:
        return cloned[id(obj)]

    if isinstance(obj, (list, tuple)):
        cloned[id(obj)] = [deepcopy(item) for item in obj]
    elif isinstance(obj, dict):
        cloned[id(obj)] = {key: deepcopy(value) for key, value in obj.items()}
    elif hasattr(obj, '__dict__'):
        clone = type(obj).__new__(type(obj))
        cloned[id(obj)] = clone

        for key, value in obj.__dict__.items():
            setattr(clone, key, deepcopy(value))

    else:
        cloned[id(obj)] = obj

    return cloned[id(obj)]


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


a = [Employee("ivan", age=24), Manager("georgi"), [1, 2, 3], Intern("stoyan"), "hello"]
b = deepcopy(a)

for original, copied in zip(a, b):
    if hasattr(original, '__dict__'):
        print(original.__dict__, "vs", copied.__dict__)
    else:
        print(original, "vs", copied)

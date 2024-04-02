class Dataclass:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args

    def __repr__(self):
        output = ', '.join(map(repr, self.args))
        return f'{self.__class__.__name__}({output})'


class Employee(Dataclass):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age

employee = Employee('Ivan', 23)
print(employee.name, employee.age)
print(repr(employee))

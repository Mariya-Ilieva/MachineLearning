def my_dataclass(cls, typecheck=False):
    initialization = cls.__init__

    def new_initialization(self, *args, **kwargs):
        initialization(self, *args, **kwargs)
        self.args = args

        if typecheck:
            for name, value in zip(cls.__annotations__.keys(), args):
                if name in kwargs:
                    value = kwargs[name]
                if not isinstance(value, cls.__annotations__[name]):
                    raise TypeError(f'Invalid type for {name}: expected {cls.__annotations__[name]}, got {type(value)}')

    setattr(cls, '__init__', new_initialization)

    def new_repr(self):
        output = ', '.join(map(repr, self.args))
        return f'{cls.__name__}({output})'

    setattr(cls, '__repr__', new_repr)

    return cls

@my_dataclass
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

employee = Employee('Ivan', 23)
print(employee.name, employee.age)
print(repr(employee))

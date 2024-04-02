def get_type(present_class):
    return list(present_class.__init__.__annotations__.values())

def convert_type(value, field_type):
    try:
        return field_type(value)
    except TypeError:
        return value

def create_object_array(class_name, data):
    cls = globals().get(class_name, None)

    if not cls:
        raise NameError(f'Class {class_name} not found.')

    lines = data.strip().split('\n')
    fields = lines[0].split(',')

    objects = []
    for i in range(1, len(lines)):
        values = lines[i].split(',')

        if len(values) != len(fields):
            raise ValueError(f'Line {i}: values for {fields} expected, but got {lines[i]}')

        converted = [convert_type(v, t) for v, t in zip(values, get_type(cls))]

        obj = cls(*converted)
        objects.append(obj)

    return objects


class Employee:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Employee(name={self.name}, age={self.age})'


data = """
name,age
Ivan,12
Dragan,15
Albena,25
"""

employees = create_object_array('Employee', data)
for e in employees:
  print(e)

e = employees[0]
print(type(e.age))
print(type(e.name))

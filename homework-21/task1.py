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

        obj = cls(*values)
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

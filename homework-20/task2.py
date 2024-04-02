class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def my_vars(obj):
    return obj.__dict__

e = Employee('Ivan', 23)
data = my_vars(e)
print(data)

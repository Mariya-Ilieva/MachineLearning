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
ea.sort()
print(', '.join([employee.name for employee in ea]))

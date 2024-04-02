def extract_str(*args):
    def extract_internal(it):
        for arg in it:
            if isinstance(arg, str):
                result.append(arg)

            elif isinstance(arg, (list, tuple, set)):
                extract_internal(arg)

            elif isinstance(arg, dict):
                extract_internal(arg.keys())
                extract_internal(arg.values())

            elif hasattr(arg, '__dict__'):
                extract_internal(arg.__dict__.values())

    result = []
    extract_internal(args)
    return result

class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


a = ['Ivan', 3, 4, 5, None]
s = extract_str(*a)
print(s)

e = Employee('Dragan')
a = ['Ivan', (3, 4), 5, e, None]
s = extract_str(*a)
print(s)

a = [3, 4, 5, None, {'Eva', 3}, 'Nikola']
s = extract_str(*a)
print(s)

a = ['Mimi', 3, 4, 5, None, [{'Eva': [3, ['Nikola']]}]]
s = extract_str(*a)
print(s)

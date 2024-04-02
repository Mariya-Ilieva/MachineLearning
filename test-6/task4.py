def a_property(type):
    def decorator(func):
        expected = len(type)

        if expected != func.__code__.co_argcount:
            raise TypeError(
                f'Function {func.__name__} expects {func.__code__.co_argcount} arguments,'
                f'but {expected} types were provided.')

        def wrapper(self):
            result = func(self)

            if not isinstance(result, type):
                raise TypeError(f'Property {func.__name__} should return {type}, but got {result}.')

            return result
        return wrapper
    return decorator

def a_setter(set_type):
    def decorator(func):
        def wrapper(self, val):

            if not isinstance(val, set_type):
                raise TypeError(f'Argument {val} is not of type {set_type} in function {func.__name__}.')

            func(self, val)

        return wrapper
    return decorator


class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @a_property
    def temperature(self):
        print('Getting value...')
        return self._temperature

    @a_setter
    def temperature(self, value):
        print('Setting value...')
        if value < -273.15:
            raise ValueError('Temperature below -273 is not possible')
        self._temperature = value

human = Celsius(37)

print(human.temperature)
print(human.to_fahrenheit())

coldest_thing = Celsius(-300)

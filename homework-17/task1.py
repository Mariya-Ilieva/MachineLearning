def accepts(*arg_types):
    for t in arg_types:
        if not isinstance(t, type):
            raise TypeError(f'{t} is not of type {type(t)}')

    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(arg_types) != len(args):
                raise TypeError(f'Function {func.__name__} expects {len(arg_types)} arguments, but {len(args)} were provided.')

            for arg, arg_type in zip(args, arg_types):
                if not isinstance(arg, arg_type):
                    raise TypeError(f'Argument {arg} is not of type {arg_type} in function {func.__name__}.')

            return func(*args, **kwargs)
        return wrapper
    return decorator

def returns(return_type):
    if not isinstance(return_type, type):
        raise TypeError(f'{return_type} is not of type {type}')

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if not isinstance(result, return_type):
                raise TypeError(f'Function {func.__name__} should return {return_type}, but got {type(result)}.')

            return result
        return wrapper
    return decorator


@accepts(int, int)
@returns(float)
def bar(low, high):
    return (low + high) * 100.10

print(bar(10, 20))
#print(bar(10.3, 20))
#print(bar(10, 20, 30))

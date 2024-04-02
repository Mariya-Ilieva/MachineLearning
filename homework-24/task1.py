def singleton(cls):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance

        if not instance:
            instance = cls(*args, **kwargs)

        return instance

    return wrapper


@singleton
class MyClass:
    pass


mc1 = MyClass()
mc2 = MyClass()

print(mc1 is mc2)

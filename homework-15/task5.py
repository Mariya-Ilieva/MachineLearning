def my_any(itr):
    for el in itr:
        if el:
            return True

    return False

my_list = [0, 0, 0]
print(my_any(my_list))

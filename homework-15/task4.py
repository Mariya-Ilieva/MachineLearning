def my_all(itr):
    for el in itr:
        if not el:
            return False

    return True

my_list =  [1, 0, 1]
print(my_all(my_list))

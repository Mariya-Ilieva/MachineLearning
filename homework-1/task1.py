for number in range(1, 101):
    if number % 5 == 0:
        if number % 3 == 0:
            print('github')
        else:
            print('hub')
    elif number % 3 == 0:
        print('git')
    else:
        print(number)

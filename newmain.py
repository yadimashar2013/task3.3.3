def test(*args):
    print(test)
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('Позиционный параметр:', i, arg)


test(11, 'spiel', [3, 2], )


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)




print(factorial(8))

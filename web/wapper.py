from functools import wraps


# 不使用wraps，那么原始函数的__name__和__doc__都会丢失
def my_decorator(fun):
    @wraps(fun)
    def wapper(*args, **kwargs):
        print('装饰器')
        return fun(*args, **kwargs)

    return wapper


@my_decorator
def myfun(name, value, age=None):
    print('myfun')
    print(name, value, age)


def mulparams(*args, **kwargs):
    print(type(args), args)  # tupe
    print(args[len(args) - 1])
    print(args[0:len(args) - 1])
    funcode = ''
    for value in args[0:len(args) - 1]:
        funcode += str(value) + '/'
    print(funcode)
    funcode = funcode[0:-1]
    print(funcode)
    print(type(kwargs), kwargs)  # dict


if __name__ == '__main__':
    # myfun(12, 23, age=123)
    print(myfun.__doc__)  
    print(myfun.__name__)
    mulparams(1, 2, 3, 4, id=1, name='jake')
    funcode = 1
    print("%s/%s"%("gateway",funcode))

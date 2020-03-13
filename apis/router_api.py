from functools import wraps


class Router:
    def __init__(self):
        self.fundict = {}  # [funcode] = function

    def route(self, *args):
        """
        args is a tuple
        """
        def decorator(func):
            funcode = ''
            for value in args:
                funcode += str(value) + "/"  # gateway/funname/request method
            self.fundict[funcode[0:-1]] = func

        return decorator

    def call(self, funcode):
        if str(funcode) in self.fundict.keys():
            func = self.fundict[str(funcode)]
            return func()
        else:
            raise Exception(f"无效路由编码:{funcode}")


if __name__ == '__main__':
    pass
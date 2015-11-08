class Test:

    def fun(self, *args, **kwargs):
        for arg in args:
            print ("arg -- > ",arg)
        
        for kwarg in kwargs:
            kwargs[kwarg] = 123
            print ("kwarg -->", kwargs[kwarg])
        args_down = [1,2,3]
        self.fun1(*args_down)

    def fun1(self, *args):
        for i, arg in enumerate(args):
            print (i, arg)

Test().fun(a = 2)

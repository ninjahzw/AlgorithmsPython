import aspectlib

@aspectlib.Aspect
def interceptor():
    print "before method execution"
    yield aspectlib.Proceed

@interceptor
def test():
    print "method execution"

test()

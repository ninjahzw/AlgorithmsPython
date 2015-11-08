

def test(func):
    def inner(value):
        print 1
        # NOTE NOTE ! Must have a return here
        return func(value)
    return inner 

#@test
#def fun2(value):
#    print value
#
#fun2(2)

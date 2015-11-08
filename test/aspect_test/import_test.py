from aspect_test import interceptor

@interceptor
def test():
    print "method execution"

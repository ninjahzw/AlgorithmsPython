from decorators_test import test

@test
def fun2(value):
    return value + 1

print fun2(2)

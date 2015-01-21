
def fizzbuzz():
    for i in xrange(1, 101):
        print i
        if i % 3 == 0:
            print 'Fizz'
        if i % 5 == 0:
            print 'Buzz'

fizzbuzz()


def fizzbuzz():
    for i in xrange(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print i, 'FizzBuzz'
            continue
        if i % 3 == 0:
            print i, 'Fizz'
            continue
        if i % 5 == 0:
            print i, 'Buzz'

fizzbuzz()

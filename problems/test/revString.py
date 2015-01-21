

def rev(ss):
    s = list(ss)
    # NOTE in python, string is immutable, has to change it to list then change back.
    length = len(s)
    mid = len(s)/2
    for i in xrange(0, mid):
        tmp = s[i]
        s[i] = s[length-1-i]
        s[length-1-i] = tmp
    return ''.join(s)
print rev('hello')

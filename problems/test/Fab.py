
# NOTE space complexity of this approach??
def fab(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fab(n-1) + fab(n-2)

def fab_dp(n):
    if n < 3:
        return n
    fabs = [0 for x in xrange(n+1)]
    fabs[1] = 1
    fabs[2] = 2
    for i in xrange(3, n+1):
        fabs[i] = fabs[i-1] + fabs[i-2]
    return fabs[n]

print fab_dp(10)

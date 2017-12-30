import decimal

decimal.getcontext().prec = 200
r2 = decimal.Decimal('2').sqrt()

def W(a, n):
    if n == 1:
        return int(a)
    if n == 0:
        return 0

    if a >= 2:
        return n * (n + 1) / 2 + W(a - 1, n)
    else:
        t = int(a * n)
        b = a / (a - 1)
        return t * (t + 1) / 2 - W(b, int(t / b))

def answer(s):
    n = int(s)
    return str(W(r2, n))


def test(s):
    n = int(s)
    r = 0
    for i in xrange(n + 1):
        r += int(r2 * i)
    return str(r)

if __name__ == '__main__':
    print answer("1")
    print answer("2")
    print answer("3")
    print answer("4")
    print answer("5")
    print answer("77")
    print answer(str(10**100))
    
    print answer(str(1000000))
    print test(str(1000000))

    exit()
    for i in xrange(20, 10000, 100):
        print i
        if answer(str(i)) != test(str(i)):
            print 'error', i
            raise Error

#!/bin/python

import sys
sys.setrecursionlimit(0x10000)
def cmax(n):
    return n * (n - 1) / 2


_cmin = {}
def cmin(n):
    if n <= 1:
        return 0
    if n not in _cmin:
        _cmin[n] = cmin((n - 1) / 2) + cmin(n - (n - 1) / 2 - 1) + (n - 1)
    return _cmin[n]


def half1(a):
    return a / 2


def half2(a):
    return a - a / 2


def get_order(l, c):
    if l == 2 and c == 1:
        return ((1, ), ())
    if l == 1 and c == 0:
        return (1,)
    if l == 0 and c == 0:
        return tuple()
    if cmin(l) <= c and cmax(l) >= c:
        now = c - l + 1
        for i in xrange(half1(l - 1) + 1):
            if now >= cmin(i) + cmin(l - i - 1) and now <= cmax(i) + cmax(l - i - 1):
                left = get_order(i, cmin(i))
                right = get_order(l - i - 1, now - cmin(i))
                if left == tuple():
                    return (right,)
                else:
                    return (left, right)
    else:
        return None
    
    
def get_number(t):
    global keyi
    if t == 1 or len(t) == 0:
        arr = []
    elif len(t) == 2:
        left = get_number(t[0])
        keyi += 1
        mid = [keyi]
        right = get_number(t[1])
        arr = mid + left + right
    elif len(t) == 1:
        left = get_number(t[0])
        keyi += 1
        mid = [keyi]
        arr = mid + left
    return arr

    
q = int(raw_input().strip())
for a0 in xrange(q):
    l,c = raw_input().strip().split(' ')
    l,c = [int(l),int(c)]
    # your code goes here
    if c > cmax(l) or c < cmin(l):
        print -1
        continue
    t = get_order(l, c)
    #print t
    keyi = 0
    print ' '.join([str(x) for x in get_number(t)])

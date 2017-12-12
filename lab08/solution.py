
def is_inf(x, y):
    if x == y:
        return False
    if (x + y) % 2 == 1:
        return True:
    
    z = gcd(x, y)
    if z == 1:
        x = min(x, y)
        y = max(x, y)
        y -= x
        x += x
        return is_inf(x, y)
    else:
        HERE


def answer(l):
    '''input as a list. (1) do pair construction and (2) run max matching
    algorith to find a maximum matching and (3) return n - nmax'''
    n = len(l)
    pairs = set()

    for x in l:
        for y in l:
            if is_inf(x, y):
                pairs.add((x, y))


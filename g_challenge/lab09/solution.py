
def __answer(b, r, bag):
    if r == 0:
        return [[False] * b]
    if b == r:
        return [[True] * b]

    result = []
    if (b - 1, r - 1) not in bag:
        bag[(b - 1, r - 1)] = __answer(b - 1, r - 1, bag)
    for tail in bag[(b - 1, r - 1)]:
        result.append([True] + tail)

    if (b - 1, r) not in bag:
        bag[(b - 1, r)] = __answer(b - 1, r, bag)
    for tail in bag[(b - 1, r)]:
        result.append([False] + tail)

    return result


def answer(b, r):
    if r == 0:
        return [[] for _ in xrange(b)]

    t = __answer(b, b - r + 1, {})
    result = [[] for i in xrange(b)]

    for i, a in enumerate(t):
        for j, b in enumerate(a):
            if b:
                result[j].append(i)
            
    return result

if __name__ == "__main__":
    for i in xrange(1, 11):
        for j in xrange(0, i + 1):
            print answer(i, j)

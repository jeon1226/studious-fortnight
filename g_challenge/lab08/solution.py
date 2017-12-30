class Node:
    def __init__(self, idx):
        self.neigh = set()
        self.idx = idx
        self.friend = None

    def addlink(self, idx):
        self.neigh.add(idx)


def order(x, y):
    return min(x, y), max(x, y)


def gcd(x, y):
    x, y = order(x, y)

    r = y % x
    if r == 0:
        return x
    else:
        return gcd(x, r)


def is_inf(x, y):
    if x == y:
        return False
    if (x + y) % 2 == 1:
        return True
    
    z = gcd(x, y)
    if z != 1:
        x /= z
        y /= z

    x, y = order(x, y)
    y -= x
    x += x
    return is_inf(x, y)


def build_matching(nodes, idx_from):
    now = nodes[idx_from]
    #print idx_from, now.neigh

    for idx_to in now.neigh:
        _next = nodes[idx_to]
        if _next.friend is None:
            if now.friend is None:
                now.friend = idx_to
                _next.friend = idx_from
            build_matching(nodes, idx_to)


def get_single_pair(nodes, idx_from):
    visited = set([idx_from])
    now = nodes[idx_from]
    path = None

    for idx_to in now.neigh:
        path = __get_single_pair(nodes, idx_to, visited)
        if path:
            path.append(now.idx)
            break
    return path


def __get_single_pair(nodes, idx_from, visited):
    if idx_from in visited:
        return None

    visited.add(idx_from)
    now = nodes[idx_from]
    if now.friend is None:
        return [now.idx]

    now = nodes[now.friend]
    visited.add(now.idx)

    for idx_to in now.neigh:
        path = __get_single_pair(nodes, idx_to, visited)
        if path:
            path.append(now.idx)
            path.append(now.friend)
            return path
    return None


def update_friend(nodes, singles, path):
    singles.remove(path[0])
    singles.remove(path[-1])

    pairs = [(path[i], path[i + 1]) for i in xrange(0, len(path), 2)]

    for i, j in pairs:
        node_i = nodes[i]
        node_j = nodes[j]

        node_i.friend = j
        node_j.friend = i


def find_max_matching(nodes):
    for node in nodes:
        if node.friend is None:
            build_matching(nodes, node.idx)
    #print_pairs(nodes)

    singles = set()
    for node in nodes:
        if node.friend is None:
            singles.add(node.idx)

    while True:
        stop_flag = True
        for single in singles:
            path = get_single_pair(nodes, single)
            if path:
                update_friend(nodes, singles, path)
                stop_flag = False
                break
        if stop_flag:
            return len(singles)
         

def print_pairs(nodes):
    for node in nodes:
        print (node.idx, node.friend)

def answer(l):
    '''input as a list. (1) do pair construction and (2) run max matching
    algorith to find a maximum matching and (3) return n - nmax'''
    n = len(l)
    pairs = set()

    for x in l:
        for y in l:
            if is_inf(x, y):
                pairs.add((x, y))

    nodes = [Node(i) for i in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            if (l[i], l[j]) in pairs:
                nodes[i].addlink(j)
                nodes[j].addlink(i)

    p = find_max_matching(nodes)
    return p


if __name__ == '__main__':
    print answer([1, 7, 3, 21, 13, 19])
    print answer([1, 1])


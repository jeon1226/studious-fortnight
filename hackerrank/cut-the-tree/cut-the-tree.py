#!/usr/bin/python3

import sys
sys.setrecursionlimit(10001)

class Node:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.neighbor = []
        self.parent = None
        self.sum = 0
        
    def addlink(self, node):
        self.neighbor.append(node)
        node.neighbor.append(self)

        
def mark(node):
    res = node.value
    if node.parent is not None:
        node.neighbor.remove(node.parent)
    for neigh in node.neighbor:
        neigh.parent = node
        res += mark(neigh)
    node.sum = res
    return res


def get_d(node, sum_all):
    res = 10**26
    for neigh in node.neighbor:
        res = min(res, get_d(neigh, sum_all))
    res = min(res, abs((sum_all - node.sum) - node.sum))
    return res
        
        
n = int(input())
v = list(map(int, input().split()))
nodes = [Node(i, v[i]) for i in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].addlink(nodes[b])

sum_all = mark(nodes[0])
print(get_d(nodes[0], sum_all))

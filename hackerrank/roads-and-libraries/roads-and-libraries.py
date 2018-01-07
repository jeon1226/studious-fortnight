#!/bin/python3

import sys

def head(a, i):
    if a[i] == i:
        return i
    else:
        return head(a, a[i])
    
    
def cluster_add(a, i, j):
    a[head(a, i)] = head(a, j)
    
    
def n_cluster(n, cities):
    a = [i for i in range(n)]
    for city in cities:
        cluster_add(a, *city)
    res = 0
    for i, x in enumerate(a):
        if i == x:
            res += 1
    return res


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return c_lib * n
    else:
        nc = n_cluster(n, cities)
        return c_road * (n - nc)  + c_lib * nc
        
        
if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m, c_lib, c_road = input().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        cities = []
        for cities_i in range(m):
            cities_t = [int(cities_temp) - 1 for cities_temp in input().strip().split(' ')]
            cities.append(cities_t)
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)

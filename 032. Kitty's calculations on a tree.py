# https://www.hackerrank.com/challenges/kittys-calculations-on-a-tree/problem?isFullScreen=true

import sys

# Build a dictionary from the 2D array that maps the key in the dict to the list of all the values it is attached to
# Eg: {1: [2, 3, 4], 2: [1], 3: [1, 5, 6, 7], 4: [1], 5: [3], 6: [3], 7: [3]}
def dict_from_edges(edges):
    d: dict[int, list[int]] = {}
    for i in range(0, len(edges)):
        d.setdefault(edges[i][0], []).append(edges[i][1])
        d.setdefault(edges[i][1], []).append(edges[i][0])
    return d
    
# Find the distance b/w a and b. d is the dictionary. visisted is the array of visited nodes
def distance(a, b, d, visited):
    if b in d[a]:
        return 1
    else:
        s = []
        visited.append(a)
        if b not in visited:
            visited.append(b)
            
        for i in d[a]:
            if i not in visited:
                if len(d[i]) == 1:
                    visited.append(i)
                else:
                    s.append(distance(i, b, d, visited))
                    visited.append(i)
        
        if s == []:
            #No path from this branch
            return sys.maxsize
        else:
            return 1 + min(s)
                


def summation(d, queries):
    answer = 0
    size = len(queries)
    for i in range(0,size):
        for j in range(i+1, size):
            visited = []
            answer = answer + queries[i]*queries[j]*distance(queries[i], queries[j], d, visited)
            
    return answer%1000000007

# Take all the inputs - n, q, edges[n-1][2], queries_size[q], queries[q][queries_size[i]]
n, q = map(int, input().split())
edges = [[] for _ in range(n-1)]        
for i in range(0, n-1):
    edges[i] = list(map(int, input().split()))

queries_size = [0]*q
queries = [[] for _ in range(q)]    
for i in range(0, q):
    queries_size[i] = int(input())
    queries[i] = list(map(int, input().split()))

# Make a dict from the edges 2D array
d = dict_from_edges(edges)

# Call the summation function for every queries[i] case
for i in range(0, q):
    result = summation(d, queries[i])
    print(result)

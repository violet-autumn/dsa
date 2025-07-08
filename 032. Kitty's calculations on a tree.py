# https://www.hackerrank.com/challenges/kittys-calculations-on-a-tree/problem?isFullScreen=true

def summation(n, edges, queries):
    
    
    
return result


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

for i in range(0, q):
    result = summation(n, edges, queries[i])
    print(result)

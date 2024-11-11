# Dynamic array with queries: https://www.hackerrank.com/challenges/dynamic-array/problem

def dynamicArray(n, queries):
    arr =  [[] for _ in range(n)] # Creates n empty arrays in the form of [[], [], []]
    lastAnswer = 0
    no_of_queries = len(queries)
    answers = []
    
    for i in range(0, no_of_queries):
        if queries[i][0] == 1:
            idx = (queries[i][1]^lastAnswer)%n
            arr[idx].append(queries[i][2])
        else:
            idx = (queries[i][1]^lastAnswer)%n
            lastAnswer = arr[idx][queries[i][2]%len(arr[idx])]
            answers.append(lastAnswer)
        
    return answers

# https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true

# Following approach works but runs into TLE
def arrayManipulation(n, queries):
    answer = [0]*(n+1)
    size = len(queries)

    for i in range (0, size):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        for j in range (a-1,b):
            answer[j] = answer[j] + k
    return max(answer)

  #-------------------------------------------------#

  #Following is the optimized approach as it avoids nested loops
  def arrayManipulation(n, queries):
    answer = [0]*(n+1)
    size = len(queries)
    
    for i in range(0, size):
        answer[queries[i][0]-1] = answer[queries[i][0]-1] + queries[i][2]
        answer[queries[i][1]] = answer[queries[i][1]] - queries[i][2]
    
    curr_value = 0    
    for i in range (0, n):
        if answer[i] != 0:
            curr_value = curr_value + answer[i]
        answer[i] = curr_value
    
    return max(answer)

"""
Suppose the input is 
n = 10
queries = [[1 5 3], [4 8 7], [6 9 1]]

This apparoach works by first only capturing the places in the answer array where the changes happen (instead of updating all the indexes in a nested manner) - 
which only takes 2 operations instead of (b-a) operations.
[3, 0, 0, 7, 0, -2, 0, 0, -7, -1, 0]

And then in the second loop it updates the values in the answer array in one go, thereby skpping extra intermediary steps 
[3, 3, 3, 10, 10, 8, 8, 8, 1, 0, 0]

Finally, we return the max.

The time complexiety of first appoach was O(nm).
The time complexiety of the second approach is O(n+m), i.e O(n)
"""

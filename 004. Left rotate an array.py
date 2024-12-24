# Left rotate an array: https://www.hackerrank.com/challenges/array-left-rotation/problem 

def rotateLeft(d, arr):
    size = len(arr)
    result = [0] * size
    for i in range(0,size):
        new_pos = (i-d)%size
        result[new_pos]=arr[i]
    return result

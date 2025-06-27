# Left rotate an array: https://www.hackerrank.com/challenges/array-left-rotation/problem 

def rotateLeft(d, arr):
    size = len(arr)
    result = [0] * size
    for i in range(0,size):
        new_pos = (i-d)%size
        result[new_pos]=arr[i]
    return result

#-----------------------------------------#

# The following appraoch reduces calculations

def rotateLeft(d, arr):
    size = len(arr)
    new_arr = [0]*size
    
    new_pos = (0-d)%size
    i = 0 
    breaker = new_pos
    
    #fill from breaker index to end of new array
    for new_pos in range (breaker,size):    
        new_arr[new_pos] = arr[i] 
        i = i+1   

    #fill for 0 to breaker index of new array
    for new_pos in range (0, breaker):       
        new_arr[new_pos] = arr[i]
        i=i+1
    
    return new_arr

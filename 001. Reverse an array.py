# Reverse a given array of integers (a) 

def reverseArray(a):
    size = len(a)
    b = []
    for i in range(0, size):
        b.append(a[size-i-1])
    return b

#----------------------------------------------#

def reverseArray(a):
    size = len(a)
    b = [0]*size
    for i in range(0, size):
        b[size-i-1]=a[i]
    return b

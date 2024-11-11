def reverseArray(a):
    size = len(a)
    # print(size)
    # print(a[size-1])
    # print(a[0])
    b = []
    for i in range(0, size):
        b.append(a[size-i-1])
    return b

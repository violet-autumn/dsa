# Find max hourglass sum in a 2D matrix

def hourglassSum(arr):
    row_size = len(arr)
    col_size = len(arr[0])
    hour_glass_sums = []
    
    for i in range(0, row_size-2):
        for j in range(0, col_size-2):
            hour_glass_sums.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
    
    return max(hour_glass_sums)

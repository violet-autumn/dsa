# Array

# Declares an empty array
a = []                   

# Appends element in the array
a.append(<elemet>) 		

# len(a) returns the length of the array 
size = len(a)				

# Creates an array b of the length "size" and initializes all elements to 0
b = [0] * size				

# Prints the array
print(a)									 

# Creates a 2D array of size rows x cols and initializes all elements with 0. Eg: [[0,0], [0,0], [0,0]]
arr = [[0 for _ in range(cols)] for _ in range(rows)]	

# Creates an empty nested 2D array. Eg: [[], [], []]
arr = [[] for _ in range(rows)]			

# Calculating row and col lengths for 2D array
row_size = len(arr)																		
col_size = len(arr[0])



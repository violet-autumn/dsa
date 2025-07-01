# Array

a = []                     														# Declares an empty appar
a.append(<elemet>) 																		# Appends element in the array
size = len(a)																					# len(a) returns the length of the array 
b = [0] * size																				# Creates an array b of the length "size" and initializes all elements to 0
print(a)																							# Prints the array

arr = [[0 for _ in range(cols)] for _ in range(rows)]	# Creates a 2D array of size rows x cols and initializes all elements with 0. Eg: [[0,0], [0,0], [0,0]]
arr = [[] for _ in range(rows)]												# Creates an empty nested 2D array. Eg: [[], [], []]
row_size = len(arr)																		# Calculating row and col lengths for 2D array
col_size = len(arr[0])



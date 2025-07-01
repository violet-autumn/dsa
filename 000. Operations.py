# Array

# Declare an empty array
a = []                   

# Append element in the array
a.append(<elemet>) 		

# len(a) returns the length of the array 
size = len(a)				

# Create an array b of the length "size" and initialize all elements 0
b = [0] * size				

# Print the array and then print the element at the 5th index
print(a)									 
print(a[i])

# Create a 2D array of size rows x cols and initialize all elements with 0. Eg: [[0,0], [0,0], [0,0]]
arr = [[0 for _ in range(cols)] for _ in range(rows)]	

# Create an empty nested 2D array. Eg: [[], [], []]
arr = [[] for _ in range(rows)]			

# Calculate row and col lengths for 2D array
row_size = len(arr)																		
col_size = len(arr[0])

#----------------------------------------------------------------------------------------------------------------------#

# Linked list

# Given pointer to head, print the "data" at all the nodes of the linked list (pointer to next node is in variable named "next")
current_node = head
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next

# Given the head, return the tail of the linked list
current_node = head
if current_node is None:
    return current_node
else:
    while current_node.next is not None:
        current_node = current_node.next
    return current_node




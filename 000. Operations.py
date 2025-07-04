# Array

# Declare an empty array
a = []                   

# Create an array of the length "size" and initialize all elements 0. Eg: [0, 0, 0]
b = [0] * size		

# Append element at the end of the array
a.append(<elemet>) 		

# Remove element from the end of the array
last_element = a.pop()

# Remove element from ith index of the array
ith_element = a.pop(i)

# Find the length of the array 
size = len(a)			

# Check if an array is empty
if a == []:
    print("The array is empty")

# Check if an element is in the array
if element in a:
    print("Element Found")
		
# Print the array and then print the element at the ith index
print(a)									 
print(a[i])

# Create a 2D array of size rows x cols and initialize all elements with 0. Eg: [[0,0], [0,0], [0,0]]
arr = [[0 for _ in range(cols)] for _ in range(rows)]	

# Create an empty nested 2D array. Eg: [[], [], []]
arr = [[] for _ in range(rows)]			

# Calculate row and col lengths for uniform 2D array
row_size = len(arr)																		
col_size = len(arr[0])

# Print values of a non-uniform 2D array in one line [[1], [2, 3], [4], [5], [6, 7, 8]]
for i in range (0, len(arr)):
	for j in range(0, len(arr[i])):
		print(arr[i][j], end=" ")

#----------------------------------------------------------------------------------------------------------------------#

# Dictionary

# Declare an empty dict
a = {}

# Assign/update the value for a given key
a[key] = value

# Print a dict
print(a)

# Find the min and max keys in a dict
min_key = min(a)
max_key = max(a)




#----------------------------------------------------------------------------------------------------------------------#

# Linked list

# Given pointer to head, print the "data" at all the nodes of the linked list (pointer to next node is in variable named "next")
current_node = head
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next

# Given pointer to head, return pointer to the tail of the linked list
if head is None or head.next is None:
    return head
else:
	current_node = head
    while current_node.next is not None:
        current_node = current_node.next
    return current_node

# Given pointer to head and data for a node, create a new node and make it the new head of the doubly linked list (pointers are prev and next)
new_node = NodeClass(data)
new_node.next = head
head.prev = new_node
head = new_node
return head

#----------------------------------------------------------------------------------------------------------------------#

# Tree

# Pre-order traversal (node, left, right)
# In-order traversal (left, node, right)
# Post-order trafversal (left, right, node)

# In-order traversal
def inOrder(root):
    if root is None:
        return;
    else:
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)

# Height of a bianry tree
def height(root):
    if root is None:
        return -1
    else:
        return 1 + max(height(root.left), height(root.right))


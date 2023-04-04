---
file_format: mystnb
kernelspec:
  name: python3
---

```{title} Graphs Data Structure & Algorithms
```

# Graphs Data Structure

## Binary Search Tree
A Binary Search Tree (BST) is a special type of binary tree in which the left child of a node has a value less than the node’s value and the right child has a value greater than the node’s value. This property is called the BST property and it makes it possible to efficiently search, insert, and delete elements in the tree.

```{image} https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221215114732/bst-21.png
:align: center
:alt: Binary Search Tree
:width: 80%
```
### Height of BST
The height of a Binary Tree is defined as the maximum depth of any leaf node from the root node. That is, it is the length of the longest path from the root node to any leaf node.


```{image} https://journaldev.nyc3.digitaloceanspaces.com/2020/01/Binary_Tree_Ht.png
:align: center
:alt: Binary Search Tree
:width: 50%
```
### Find in BST

Complexity: O(log n) and O(n) in worst case


### Insertion and Deleteion in BST

```{code-cell}
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end =" ")
        inorder(root.right)


if __name__ == '__main__':

    # Let us create the following BST
    # 50
    #  /     \
    # 30     70
    #  / \ / \
    # 20 40 60 80

    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    # Print inorder traversal of the BST
    inorder(r)

```


Delete a node from BST

```{code-cell}
# Python program to demonstrate delete operation
# in binary search tree

# A Binary Tree Node


class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# A utility function to do inorder traversal of BST
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)


# A utility function to insert a
# new node with given key in BST
def insert(node, key):

	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node

# Given a non-empty binary
# search tree, return the node
# with minimum key value
# found in that tree. Note that the
# entire tree does not need to be searched


def minValueNode(node):
	current = node

	# loop down to find the leftmost leaf
	while(current.left is not None):
		current = current.left

	return current

# Given a binary search tree and a key, this function
# delete the key and returns the new root


def deleteNode(root, key):

	# Base Case
	if root is None:
		return root

	# If the key to be deleted
	# is smaller than the root's
	# key then it lies in left subtree
	if key < root.key:
		root.left = deleteNode(root.left, key)

	# If the kye to be delete
	# is greater than the root's key
	# then it lies in right subtree
	elif(key > root.key):
		root.right = deleteNode(root.right, key)

	# If key is same as root's key, then this is the node
	# to be deleted
	else:

		# Node with only one child or no child
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		# Node with two children:
		# Get the inorder successor
		# (smallest in the right subtree)
		temp = minValueNode(root.right)

		# Copy the inorder successor's
		# content to this node
		root.key = temp.key

		# Delete the inorder successor
		root.right = deleteNode(root.right, temp.key)

	return root


# Driver code
""" Let us create following BST
			50
		/	 \
		30	 70
		/ \ / \
	20 40 60 80 """

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = deleteNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)



```
### Traversals – Inorder, Preorder, Post Order
Given a Binary Search Tree, The task is to print the elements in inorder, preorder, and postorder traversal of the Binary Search Tree. 


```{image} https://media.geeksforgeeks.org/wp-content/uploads/20220730030128/Screenshot20220730at30104AM-660x431.png
:align: center
:alt: Binary Search Tree
:width: 70%
```

Inorder Traversal: 10 20 30 100 150 200 300

Preorder Traversal: 100 20 10 30 200 150 300

Postorder Traversal: 10 30 20 150 300 200 100

#### Inorder Traversal:

Traverse left subtree
Visit the root and print the data.
Traverse the right subtree


```{code-cell}
class Node:
	def __init__(self, v):
		self.left = None
		self.right = None
		self.data = v

# Inorder Traversal
def printInorder(root):
	if root:
		# Traverse left subtree
		printInorder(root.left)
		
		# Visit node
		print(root.data,end=" ")
		
		# Traverse right subtree
		printInorder(root.right)

# Driver code
if __name__ == "__main__":
	# Build the tree
	root = Node(100)
	root.left = Node(20)
	root.right = Node(200)
	root.left.left = Node(10)
	root.left.right = Node(30)
	root.right.left = Node(150)
	root.right.right = Node(300)

	# Function call
	print("Inorder Traversal:",end=" ")
	printInorder(root)

	# This code is contributed by ajaymakvana.
```

#### Preorder Traversal
At first visit the root then traverse left subtree and then traverse the right subtree.

Follow the below steps to implement the idea:

- Visit the root and print the data.
- Traverse left subtree
- Traverse the right subtree


```{code-cell}
class Node:
	def __init__(self, v):
		self.data = v
		self.left = None
		self.right = None

# Preorder Traversal
def printPreOrder(node):
	if node is None:
		return
	# Visit Node
	print(node.data, end = " ")

	# Traverse left subtree
	printPreOrder(node.left)

	# Traverse right subtree
	printPreOrder(node.right)

# Driver code
if __name__ == "__main__":
	# Build the tree
	root = Node(100)
	root.left = Node(20)
	root.right = Node(200)
	root.left.left = Node(10)
	root.left.right = Node(30)
	root.right.left = Node(150)
	root.right.right = Node(300)

	# Function call
	print("Preorder Traversal: ", end = "")
	printPreOrder(root)

```

#### Postorder Traversal
At first traverse left subtree then traverse the right subtree and then visit the root.

Follow the below steps to implement the idea:

- Traverse left subtree
- Traverse the right subtree
- Visit the root and print the data.

```{code-cell}

class Node:
	def __init__(self, v):
		self.data = v
		self.left = None
		self.right = None

# Preorder Traversal
def printPostOrder(node):
	if node is None:
		return

	# Traverse left subtree
	printPostOrder(node.left)

	# Traverse right subtree
	printPostOrder(node.right)
	
	# Visit Node
	print(node.data, end = " ")

# Driver code
if __name__ == "__main__":
	# Build the tree
	root = Node(100)
	root.left = Node(20)
	root.right = Node(200)
	root.left.left = Node(10)
	root.left.right = Node(30)
	root.right.left = Node(150)
	root.right.right = Node(300)

	# Function call
	print("Postorder Traversal: ", end = "")
	printPostOrder(root)


```
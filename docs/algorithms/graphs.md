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
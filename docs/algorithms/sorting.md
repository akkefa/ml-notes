---
file_format: mystnb
kernelspec:
  name: python3
---

```{title} Sorting Algorithms
```

# Sorting Algorithms


```{image} https://zaxrosenberg.com/wp-content/uploads/2017/12/sort_complexity.png
:align: center
:alt: Insertion Sort
:width: 80%
```

## Insertion Sort
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

### Characteristics of Insertion Sort
- This algorithm is one of the simplest algorithm with simple implementation
- Basically, Insertion sort is efficient for small data values
- Insertion sort is adaptive in nature, i.e. it is appropriate for data sets which are already partially sorted.


```{image} https://media.geeksforgeeks.org/wp-content/uploads/insertionsort.png
:align: center
:alt: Insertion Sort
:width: 50%
```
---

```{image} https://www.swtestacademy.com/wp-content/uploads/2021/11/insertion-sort.gif
:align: center
:alt: Insertion Sort
:width: 80%
```

### Implmentation

```bash
procedure insertionSort(A: list of sortable items)
   n = length(A)
   for i = 1 to n - 1 do
       j = i
       while j > 0 and A[j-1] > A[j] do
           swap(A[j], A[j-1])
           j = j - 1
       end while
   end for
end procedure
```

```{code-cell}

def insertion_sort(data: list):
    
    print(f"Unsorted List: {data}")

    for i in range(1, len(data)):
        print("===" * 10)
        print(f"Iteration: {i} & Current Element: {data[i]}")
        
        key = data[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1

        while j >= 0 and key < data[j] :
                print(f"j = {j}")
                print(f"Swapping {data[j]} with {data[j + 1]}")
                data[j + 1] = data[j]
                j -= 1
                print(f"Swapped List: {data}")
        
        print(f"Inserting {key} at position {j + 1}")
        data[j + 1] = key
        print(f"New List: {data}")
        print("===" * 10)
    
    return data
 
insertion_sort([12, 11, 13, 5, 6])

print("####" * 10)

insertion_sort([6, 11, 6, 44, 6,7,9,22,0])
 
# This code is contributed by Mohit Kumra
```
## Merge sort

Merge sort is a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.

In simple terms, we can say that the process of merge sort is to divide the array into two halves, sort each half, and then merge the sorted halves back together. This process is repeated until the entire array is sorted.

```{image} https://i0.wp.com/www.coderarticles.com/wp-content/uploads/2019/01/merge_sort_algorithm.png
:align: center
:alt: Merge Sort
:width: 80%
```

The “Merge Sort”  uses a recursive algorithm to achieve its results.

### Advantages of the Merge Sort

- Merge sort can efficiently sort a list in O(n*log(n)) time.
- Merge sort can be used with linked lists without taking up any more space.
- A merge sort algorithm is used to count the number of inversions in the list.
- Merge sort is employed in external sorting.

### Drawbacks of the Merge Sort

- For small datasets, merge sort is slower than other sorting algorithms.
- For the temporary array, mergesort requires an additional space of O(n).
- Even if the array is sorted, the merge sort goes through the entire process.

### Python implementation of MergeSort

```{code-cell}
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

arr = [12, 11, 13, 5, 6, 7]
print(arr)
mergeSort(arr)
print(arr)
```

## Binary Search

Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n). 


```{image} https://blog.penjee.com/wp-content/uploads/2015/04/binary-and-linear-search-animations.gif
:align: center
:alt: Binary Search
:width: 80%
```

### python Implmentation of Binary Search

```{code-cell}

def binarySearchHelper(lst, elt, left, right):
    n = len(lst)
    if (left > right):
        return None # Search region is empty -- let us bail since we cannot find the element elt in the list.
    else: 
        # If elt exists in the list, it must be between left and right indices.
        mid = (left + right)//2 # Note that // is integer division 
        if lst[mid] == elt: 
            return mid # BINGO -- we found it. Return its index signalling that we found it.
        elif lst[mid] < elt: 
            # We search in the right part of the list
            return binarySearchHelper(lst, elt, mid+1, right)
        else: # lst[mid] > elt
            # We search in the left part of the list.
            return binarySearchHelper(lst, elt, left, mid-1)

def binarySearch(lst, elt):
    n = len(lst)
    if (elt < lst[0] or elt > lst[n-1]):
        return None
    else: # Note: we will only get here if
          # lst[0] <= elt <= lst[n-1]
        return binarySearchHelper(lst, elt, 0, n-1)

print("Searching for 9 in list [0,2,3,4,6,9,12]")
print(binarySearch([0,2,3,4,6,9,12], 9))

print("Searching for 8 in list [1, 3, 4, 6, 8, 9,10, 11, 12, 15]")
print(binarySearch([1, 3, 4, 6, 8, 9,10, 11, 12, 15], 8))

print("Searching for 5 in list [1, 3, 4, 6, 8, 9,10, 11, 12, 15]")
print(binarySearch([1, 3, 4, 6, 8, 9,10, 11, 12, 15], 5))

print("Searching for 0 in list [0,2]")
print(binarySearch([0,2], 0))

print("Searching for 1 in list [0,2]")
print(binarySearch([0,2], 1))

print("Searching for 2 in list [0,2]")
print(binarySearch([0,2], 2))

print("Searching for 1 in list [1]")
print(binarySearch([1], 1))

print("Searching for 2 in list [1]")
print(binarySearch([1], 2))

```
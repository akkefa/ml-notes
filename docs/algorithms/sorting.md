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

# Function to do insertion sort
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
 
# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
 
# This code is contributed by Mohit Kumra
```
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
:alt: Sort Complexity
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
### Pseudo Code

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
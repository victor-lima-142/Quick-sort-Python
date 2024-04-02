# Explanation of methods

1.  **quick_sort(arr)**: This is the entry point for the quick sort algorithm. It calls the helper function `quick_sort_helper` to sort the entire array `arr`.
    
2.  **quick_sort_helper(arr, low, high)**: This function implements the recursive part of the quick sort algorithm. It takes an array `arr`, and the indices `low` and `high` which represent the range of elements to be sorted. It partitions the array around a pivot element and recursively sorts the two partitions.
    
3.  **partition(arr, low, high)**: This function partitions the array `arr` around a pivot element. It takes an array `arr`, and the indices `low` and `high` which represent the range of elements to be partitioned. It chooses the pivot element (in this case, the rightmost element), and rearranges the elements such that all elements less than or equal to the pivot are on the left side, and all elements greater than the pivot are on the right side. It then returns the index of the pivot element after partitioning.

# Concepts
1. **Entry Point**: First method that run all logic of algorithm.
2. **Recursive method**: Is a method that calls itself. 

> This concept of recursive method was taken from the book "Classic Computer Science Problems in Python" by David Kopec by Manning (page 22)

3. **Partition**: The partition function in a sorting algorithm is a crucial step that divides an array into two parts, so that all elements in one part are smaller (or equal) than a certain value, known as the pivot, and all elements in the other part are greater than this pivot. Essentially, the partition function rearranges the array elements in such a way that the pivot occupies its correct position in the final order of the sorted array.
The goal of partitioning is to facilitate the subsequent sorting of elements, because after partitioning, the pivot will be in its final position, and will not need to be moved again.
The choice of pivot may vary depending on the sorting algorithm. In some cases, the pivot is simply the first element of the array, the last element, or a random element. In the Quick Sort algorithm, for example, the pivot is often chosen as the last element of the array.
During partitioning, the array elements are rearranged in such a way that:
--   All elements smaller or equal to the pivot are located to the left of the pivot.
--   All elements greater than the pivot are located to the right of the pivot.
After partitioning, the pivot is in its final position in the sorting, and the array has been divided into two parts. These two parts can then be sorted independently, which is done recursively in the case of the Quick Sort algorithm.
In summary, the partition function is a crucial step in many sorting algorithms, where it divides the array into two parts around a pivot, facilitating the subsequent sorting of elements.

# About complexity
The complexity of the Quick Sort algorithm is crucial to understanding its efficiency. There are two main complexity metrics to consider: time complexity and space complexity.

1.  **Time Complexity**:
    
    -   Quick Sort is known for its average efficiency and is generally very fast in practice. Its average time complexity is O(n log n), where "n" is the number of elements to be sorted.
    -   However, the worst-case time complexity occurs when the chosen pivot does not evenly divide the input set, leading to an unbalanced array partition. In these cases, the time complexity can become O(n^2), where "n" is the number of elements. This usually happens when the array is nearly sorted or when all elements are equal.
    -   Nevertheless, the occurrence of worst-case time complexity is rare in practice and can be mitigated by choosing a random pivot or adopting other pivot selection strategies.
2.  **Space Complexity**:
    
    -   The space complexity of Quick Sort is O(log n) due to recursion. This is because, in each recursive call, the call stack of the partition function increases, but the maximum depth of the call stack is logarithmic in relation to the number of elements "n". This means that Quick Sort is efficient in terms of memory usage.

Additionally, Quick Sort is an in-place algorithm, which means it does not require additional memory to perform sorting. It sorts the elements in the input array itself, modifying the elements of the array without using additional memory.

In summary, Quick Sort is an efficient algorithm in terms of time (on average) and space, making it a popular choice for sorting large datasets in practice. However, it is important to be aware of the possibility of extreme cases of time complexity and take measures to mitigate them if necessary.

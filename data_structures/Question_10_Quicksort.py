"""
Question #10 - Quicksort

Write a quicksort algorithm for an array of sorted numbers.  

Example:

Sample Input 1:
> [2, 5, 1, 3, 8]  

Sample Output 1:
> [1, 2, 3, 5, 8]  
"""

# Taken from https://www.educative.io/answers/how-to-implement-quicksort-in-python

def QuickSort(arr):
    elements = len(arr)
    
    # Base case, if list has 1 element only.
    if elements < 2:
        return arr
    
    current_position = 0  # Position of the partitioning element.

    for i in range(1, elements):  # Partitioning loop.
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp  # Brings pivot to it's appropriate position.
    
    left = QuickSort(arr[0:current_position])  # Sorts the elements to the left of pivot.
    right = QuickSort(arr[current_position+1:elements])  # Sorts the elements to the right of pivot.

    arr = left + [arr[current_position]] + right  # Merging everything together.
    
    return arr


array_to_be_sorted = [4,2,7,32,1,61]
print("Original Array:", array_to_be_sorted)
print("Sorted Array:", QuickSort(array_to_be_sorted))

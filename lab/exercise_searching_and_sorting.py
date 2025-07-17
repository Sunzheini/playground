# ------------------------------------------------------------------
# 1. Linear search
# ------------------------------------------------------------------

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


print(linear_search([10, 20, 30, 40, 50], 30))


# ------------------------------------------------------------------
# 2. Binary search: find the index of a target value in a sorted array
# ------------------------------------------------------------------

def binary_search(arr, target):
    """Perform binary search on a sorted array to find the index of the target value."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target was not found in the array
    return -1


print(binary_search([10, 20, 30, 40, 50], 30))


# ------------------------------------------------------------------
# 3. Selection sort: simple but inefficient sorting algorithm
# ------------------------------------------------------------------

def selection_sort(arr):
    """Sort an array using the selection sort algorithm."""
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(selection_sort([64, 25, 12, 22, 11]))


# ------------------------------------------------------------------
# 4. Bubble sort: swapping to neighboring elements until sorted
# ------------------------------------------------------------------

def bubble_sort(arr):
    """Sort an array using the bubble sort algorithm."""
    n = len(arr)
    for i in range(n):
        # Track if a swap was made
        swapped = False
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped, the array is sorted
        if not swapped:
            break

    return arr


print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))


# ------------------------------------------------------------------
# 5. Insertion sort: building a sorted array one element at a time
# ------------------------------------------------------------------

def insertion_sort(arr):
    """Sort an array using the insertion sort algorithm."""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


print(insertion_sort([12, 11, 13, 5, 6]))


# ------------------------------------------------------------------
# 6. Quick sort: divide and conquer sorting algorithm, efficient for large datasets
# ------------------------------------------------------------------

def quick_sort(arr):
    """Sort an array using the quick sort algorithm."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


print(quick_sort([3, 6, 8, 10, 1, 2, 1]))


# ------------------------------------------------------------------
# 7. Merge sort
# ------------------------------------------------------------------

def merge_sort(arr):
    """Sort an array using the merge sort algorithm."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))



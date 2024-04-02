def quick_sort(arr):
    sort(arr, 0, len(arr) - 1)

def sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        sort(arr, low, pivot_index - 1)
        sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot_value = arr[high]
    pivot_index = low - 1

    for j in range(low, high):
        if arr[j] <= pivot_value:
            pivot_index += 1
            arr[pivot_index], arr[j] = arr[j], arr[pivot_index]

    arr[pivot_index + 1], arr[high] = arr[high], arr[pivot_index + 1]
    return pivot_index + 1

#Tests
arr = [1,3,6,4,2,5]
print(f"Array before sort: {arr}")

quick_sort(arr)
print(f"Array after sort: {arr}")
# QUICK SORT ALGORITHM
    
def sorting(arr, left, right):
    if left < right:
        partion_pos = partition(arr, left, right)
        sorting(arr, left, partion_pos - 1)
        sorting(arr, partion_pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1

        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]


    return i

arr = [3,1,7,5,9]
sorting(arr, 0, len(arr) - 1)

print(arr)

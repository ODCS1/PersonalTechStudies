# BUBBLE SORT

class BubbleSort:
    def sorting(self, arr):
        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    aux = arr[i]
                    arr[i] = arr[j]
                    arr[j] = aux



arr = [5, 1, 7, 9, 11, 3, 2]
obj = BubbleSort()
obj.sorting(arr)
print(arr)
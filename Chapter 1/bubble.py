def bubble(arr):
    print(arr)
    # Traverses through all elements in the array
    for i in range(len(arr)):
        # Traverses through all elements not already sorted
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


print(bubble([4, 3, 2, 1]))

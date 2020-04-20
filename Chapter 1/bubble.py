def bubble(arr):
    print(arr)
    # Interate through each item in the array
    for i in range(len(arr)):
        # Loop through each item not sorted i.e. when i=0 no items are sorted, i=1 the last item is sorted ect...
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


print(bubble([4, 3, 2, 1]))

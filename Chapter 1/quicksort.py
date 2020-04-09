# During an execution you get a binary tree
# Hence O(n) = log_2(n)
def quicksort(arr): 
    lower = []
    equal = []
    higher = []
    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                lower.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                higher.append(x)
        # Using a recursive function
        # Whilst you continue to algorithm is executed a binary tree is made
        return quicksort(lower) + equal + quicksort(higher)
    return arr


print(quicksort([4, 3, 2, 1]))

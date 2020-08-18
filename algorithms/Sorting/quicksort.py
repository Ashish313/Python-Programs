
def partitions(arr, start, end):
    i = start-1
    pivot = arr[end]                # choose last element of array as pivot
    for j in range(start,end):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]

    # move the pivot at its correct position
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return (i+1)


def quicksort(arr,start,end):
    if start < end:
        p = partitions(arr,start,end)

        # sort elements before and after partition
        quicksort(arr, start, p-1)
        quicksort(arr, p+1, end)

    return arr


# driver code
arr = [103,7,8,67,9,154,1,29,5,75]

print(f'Given array: {arr}')
quicksort(arr, 0, len(arr)-1)
print(f'Sorted array : {arr}')


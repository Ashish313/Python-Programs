
def mergesort(arr):
    if len(arr) > 1:

        # find the middle point and divide the array into two parts
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        # repeat the same procedure for left array and right array
        mergesort(L)
        mergesort(R)
        i = j = k = 0

        # compare the elements of left and right array
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

            k += 1

        # check for remaining elements of left array if any
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # check for remaining elements of right array if any
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


# driver code
if __name__ == '__main__':
    arr = [91,12,11,87,28,13,5,33,63,7,13]
    print(f'Given array: {arr}')
    mergesort(arr)
    print(f'Sorted array: {arr}')


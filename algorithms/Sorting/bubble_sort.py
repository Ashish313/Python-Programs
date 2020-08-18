
def bubble_sort(arr):
    for i in range(len(arr)):
        swapped=False

        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        
        # check if no swapping takes place in the first loop over the array
        # in case of already sorted array
        if swapped==False:
            break

    return arr


# driver code
if __name__ == '__main__':
    arr = [56,3,14,78,22,4,40,5,82,1,90]
    print(f'Given array: {arr}')
    arr = bubble_sort(arr)
    print(f'Sorted array: {arr}')
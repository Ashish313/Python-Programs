
def selection_sort(arr):
    for i in range(len(arr)):

        # find minimum element in the remaining array
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[min_index],arr[i] = arr[i],arr[min_index]

    return arr


# driver code
if __name__ == '__main__':
    arr = [56,18,63,51,78,23,5,113,0,90,1,87]
    
    print(f'Given array: {arr}')
    selection_sort(arr)
    print(f'Sorted array: {arr}')


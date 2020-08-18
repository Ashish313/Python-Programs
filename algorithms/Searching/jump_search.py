import math


# jump search algorithm searches for an element in a sorted array
# if the array is not sorted, sort the array first

def jump_search(arr,number):
    size = len(arr)
    step = math.sqrt(size)            # size of jump
    prev = 0

    # find the subarray according to the number
    while arr[int(min(step,size)-1)] < number:
        prev = step
        step += math.sqrt(size)

        if prev >= size:
            return -1

    # look for the number in the subarray
    while arr[int(prev)] < number:
        prev += 1

        if prev == min(step,size):
            return -1

    if arr[int(prev)] == number:
        return prev

    return -1


# driver code
if __name__ == '__main__':
    arr=[0,1,2,2,3,5,8,13,21,34,55,89,144,240,377,412,433]
    number=int(input('Enter the number you want to search: '))
    index=int(jump_search(arr,number))
    
    if abs(index) == index:
        print(f'{number} is at index {index}.')

    else:
        print(f'{number} is not present in the list.')

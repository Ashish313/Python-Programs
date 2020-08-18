# binary search algorithm searches for an element in a sorted array
# if the array is not sorted, sort the array first

def binary_search(my_list,number):
    start = 0
    end = len(my_list)-1

    while start <= end:

        # find the mid point of the list
        mid = (start+end)//2

        if my_list[mid] == number:
            print(f'{number} is at index: {mid}')
            break

        elif my_list[mid] > number:
            end=mid-1               
            
        elif my_list[mid] < number:
            start=mid+1

    else:
        print(f'{number} is not in the list.')


# driver code
my_list=[2,7,19,34,53,72,88]
number=int(input('Enter the number you want to search: '))

binary_search(my_list, number)

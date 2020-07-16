# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start=0, end=None):
    
    if end is None:
        end = len(arr) -1
    if start > end:
        return target#f"{target} not found in list"
    else:
        mid = (start + end)//2
        if target == arr[mid]:
            return mid #f"{target} found at index: {mid}"
        elif target > arr[mid]:
           return binary_search(arr,target,mid+1,end)
        else:
            return binary_search(arr,target,start,mid-1)

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass


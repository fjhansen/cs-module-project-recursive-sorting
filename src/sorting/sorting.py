# TO-DO: complete the helper function below to merge 2 sorted arrays
##def merge(arrA, arrB):
##    merged_arr = []
##    i, j = 0, 0
##
##    while i < len(arrA) and j < len(arrB):
##        if arrA[i] < arrB[j]:
##            merged_arr.append(arrA[i])
##            i += 1
##        else:
##            merged_arr.append(arrB[j])
##            j += 1
##
##    while i < len(arrA):
##        merged_arr.append(arrA[i])
##        i+=1
##    while j < len(arrB):
##        merged_arr.apped(arrB[j])
##        j+=1
##
##
##    return merged_arr



def merge(arr1, arr2):
    print("merge function called with lists below: \n")
    print(f"left: {arr1} \nright: {arr2}\n")
    sorted_arr = []
    i, j = 0, 0
    # 2
    while i < len(arr1) and j < len(arr2):
            print(f"\nLeft-list-index-i: {i}\nLeft-list-index-value: {arr1[i]}\n")

            print(f"Right-list-index-j: {j}\nRight-list-index-value: {arr2[j]}\n")


        # 1.
            if arr1[i] < arr2[j]:
                sorted_arr.append(arr1[i])
                # 3.
                i += 1
            else:
                sorted_arr.append(arr2[j])
                # 3.
                j += 1
            print(f"{sorted_arr}\n")
            print("="*50)
    #4
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1  
        

    
    return sorted_arr

# Steps
#1. Compare first element in each list and append the smaller element
#2. iterate through all items until you reach the end of the list.
#2. iteration includes using the comparison in #1 for all elements in both lists

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7,3000]
arr2 = [300,100]

print(f"Merged-List: {merge(arr1,arr2)}")

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    # 1.
    if len(arr) <= 1:
        return arr
    
    # 2.
    mid = len(arr)//2
    
    # 3.  
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])

    # 4.
    arr = merge(left,right)


    return arr

# 1. return array if there is only one element
# 2. divide in half
# 3. merge sort both halves of array
# 4. merge using first function

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

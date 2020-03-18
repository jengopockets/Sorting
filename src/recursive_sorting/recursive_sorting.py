# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    #loop through index of our added array size
    for i in range(0, elements):
        #Check first possition in both arrays
        if arrA == []: #Checks to see if array A is empty
            merged_arr[i] = arrB[0]
            arrB.remove(arrB[0])
        elif arrB == []: #Checks if array B is empty
            merged_arr[i] = arrA[0]
            arrA.remove(arrA[0])
        elif arrA[0] < arrB[0]:
            #make merged_arr index equal lowest variable
            merged_arr[i] = arrA[0]
            #remove index from original array
            arrA.remove(arrA[0])

        else:
            merged_arr[i] = arrB[0]
            arrB.remove(arrB[0])

    # TO-DO
    
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
#Split list function
def split(a_list):
    if len(a_list) == 1:#Checks if the list can be split
        pass
    else:
        half = len(a_list)//2 #Splits in half
        return a_list[ 0 :half], a_list[half:] #Returns both halves

        
def merge_sort( arr ):
    
    
    if len(arr) > 1:#checks for elements in the array
        A, B = split(arr)#Uses split function to split the array
        left = merge_sort(A)#Splits first half
        right = merge_sort(B)#Splits second half
        arr = merge(left, right)#Merges the two halves
    

    
    # TO-DO

    return arr

# print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

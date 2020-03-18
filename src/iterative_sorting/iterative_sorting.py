# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for num in range(cur_index, len(arr)):
            if arr[num] < arr[smallest_index]:
                smallest_index = num
             



        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp




    return arr
arr_sort = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(selection_sort(arr_sort))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:

                #swap point
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swap = True

    return arr


print(bubble_sort(arr_sort))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
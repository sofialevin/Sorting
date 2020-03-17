# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range (cur_index, len(arr) - 1):
            # compares value of smallest index with value of next array item
            if arr[smallest_index] > arr[j + 1]:
                smallest_index = j + 1

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


my_list = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(selection_sort(my_list))

# # TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):
#     for i in arr:
#         if i > i + 1:




#     return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr
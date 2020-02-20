# TO-DO: Complete the selection_sort() function below
arry = [12, 34, 15, 75, 4, 9]


print("\n============ selection Sorting====================")


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        print(arr)

    return arr


selection_sort(arry)


# TO-DO:  implement the Bubble Sort function below
arr = [12, 34, 15, 75, 4, 9]

print("\n============ Bubble Sorting====================")


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)

    return arr


bubble_sort(arr)
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr

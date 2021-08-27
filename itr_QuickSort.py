"""

Implementation credit goes to : CSDoJo and Mohit Kumra from GeeksForGeeks

This is the iterative implementation of the quickSort algorithm.

This version of the algorithm is likely to be more pratical and useful in professional programming, as iterative algorithmns
have none of the downsides of recursive algorithms (memory liminations).



Some notes about the iterative version of QuickSort:


We have two iteration pointers : i and j

if we pick our pivot to be the last number, we want j to traverse from element 0 to the last element before the privot (len) - 1?

iteration pointer i should delienate the elements smaller than the pivot.

"""


"""

performs the partition part of the quick sort function

"""


def partition(arr, l, h):
    i = ( l - 1 )
    x = arr[h]
 
    for j in range(l, h):
        if   arr[j] <= x:
 
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)

def QuickSort(arr_list, l, h):
    print("Calling QuickSort...")

    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
 
    # initialize top of stack
    top = -1
 
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, l, h )
 
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h




# Driver code to test above
arr = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(arr)
QuickSort(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print ("% d" % arr[i]),
 
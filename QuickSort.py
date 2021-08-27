"""

This is the implementation fo the QuickSort Algorithmn in its most basic form (recursive, static pivot selection).




"""

# the starthing index and ending_index refer to the section of the array that we want to sort

def partition(arr, starting_index, ending_index):
    i = (starting_index - 1)
    pivot = arr[ending_index]

    for j in range(starting_index,ending_index):
        if (arr[j] <= pivot):
            i += 1
            #swapping the contents
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[ending_index] = arr[ending_index],arr[i + 1]
    return (i+1)



# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index




def qs(arr, l, h):
    # base case. If both indexes point to 1 element (1 elem? the elem must be sorted) or 0 elem (no elem? Nothing to sort)
    # then we have nothing to do. Return
    if( l >= h):
        return
    # we must obtain a pivot
    p = partition(arr, l , h)

    # sorting all elements below the pivot
    qs(arr,l, p-1)

    # sorting all elements above the pivot
    qs(arr, p + 1, h)
 
 


"""
arrrr = [9,4,9,4444,55,399,46,23,12,76]


qs(arrrr, 0, len(arrrr) - 1)

print(arrrr)

"""
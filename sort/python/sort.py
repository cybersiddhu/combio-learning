"""Functions for various sorting algorithms """


def bubblesort_descending(numlist):
    """ In place descending bubble sort """
    for passnumlist in range(len(numlist) - 1, 0, -1):
        for i in range(passnumlist):
            if numlist[i] < numlist[i + 1]:
                numlist[i + 1], numlist[i] = numlist[i], numlist[i + 1]


def bubblesort_ascending(numlist):
    """ In place ascending bubble sort """
    for passnumlist in range(len(numlist) - 1, 0, -1):
        for i in range(passnumlist):
            if numlist[i] > numlist[i + 1]:
                numlist[i + 1], numlist[i] = numlist[i], numlist[i + 1]


def selectionsort_ascending(numlist):
    """
    In place selection sort
    """
    #in each pass,the index run in reverse
    #the value of fillslot variable in each pass is the position
    #where highest value should be placed
    for fillslot in range(len(numlist) - 1, 0, -1):
        maxpos = 0
        for loc in range(1, fillslot + 1):
            #find the index with highest value
            if numlist[loc] > numlist[maxpos]:
                maxpos = loc
            #put them in correct position by swapping
            numlist[fillslot], numlist[maxpos] = numlist[maxpos], numlist[fillslot]
    return True


def insertionsort_ascending(numlist):
    """In place insertion sort"""
    for loc in range(1, len(numlist)):
        # this variable(pos) tracks the index as the item in the list
        # moves back after each comparison
        pos = loc
        # this variable(item) holds the item in the list until
        # it gets the location to be inserted
        item = numlist[loc]
        inner = True
        while pos > 0 and inner:
            # this if block keeps shifting item forward
            if item < numlist[pos - 1]:
                #exchange position of items
                numlist[pos] = numlist[pos - 1]
                pos = pos - 1
            else:
                # no more comparison needed, the rest
                # of the list is already sorted
                inner = False
        if loc != pos:
            numlist[pos] = item

    return True


def shellsort_ascending(numlist, gapseq=None):
    """In place shell sort
    """
    if gapseq is None:
        gapseq = [701, 301, 132, 57, 23, 10, 4, 1]
    else:
        if type([]) != type(gapseq):
            gapseq = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gapseq:
        #now it's basically an insertion sort using the gap value
        outer = True
        while gap < len(numlist) and outer:
            for loc in range(gap, len(numlist)):
                pos = loc
                item = numlist[loc]
                inner = True
                while pos > gap - 1 and inner:
                    if item < numlist[pos - gap]:
                        numlist[pos] = numlist[pos - gap]
                        pos = pos - gap
                    else:
                        inner = False
                if loc != pos:
                    numlist[pos] = item
            outer = False

    return True


def mergesort_ascending(numlist):
    """
       Runs merge sort and returns a new sorted list
       with identical elements
    """
    # By running the unit tests after commenting out the print
    # statements it could be observed
    # that the recursion stops when this method gets called with a single
    # element. So, the first called to mergelist method is with two single
    # element lists.
    # The two single element lists returns a sorted two element list.
    # This will finish the unravel the first series of recursion
    # that ends with the left variable getting  the two element list.
    # Similarly, the right variable will receive another two element
    # list after another set of recursive calls. After, that the
    # mergelist would return a sorted four element list.
    # Overall, the above steps gets repeated as all recursive called
    # get unraveled and ends with returning a fully sorted list.
    #print("called", numlist)
    if len(numlist) < 2:
        return numlist

    middle = len(numlist) // 2

    left = mergesort_ascending(numlist[:middle])
    right = mergesort_ascending(numlist[middle:])
    #print("left:", left, " right:", right)
    sortedlist = mergelist(left, right)
    #print("got ", sortedlist)
    return sortedlist


def mergelist(left, right):
    """
    Returns a newly sorted list by merging the two input list

    left
        A sorted list
    right
        Another sorted list

    """
    i, j = 0, 0
    result = []
    # Here two separate sorted list(left and right) are repeatedly
    # compared to each other and
    # the least value is removed and appended to a new list(result).
    # Actually, instead of modifying the lists(left and right),
    # their pointer(i and j)  are incremented instead after every
    # comparison
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # When one of them is exhausted the rest of the elements are appended
    # from the other list
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])
    return result

"""Functions for various sorting algorithms """


def bubblesort_descending(num):
    """ In place descending bubble sort """
    for passnum in range(len(num) - 1, 0, -1):
        for i in range(passnum):
            if num[i] < num[i + 1]:
                num[i + 1], num[i] = num[i], num[i + 1]


def bubblesort_ascending(num):
    """ In place ascending bubble sort """
    for passnum in range(len(num) - 1, 0, -1):
        for i in range(passnum):
            if num[i] > num[i + 1]:
                num[i + 1], num[i] = num[i], num[i + 1]


def selectionsort_ascending(num):
    """
    In place selection sort
    """
    #in each pass,the index run in reverse
    #the value of fillslot variable in each pass is the position
    #where highest value should be placed
    for fillslot in range(len(num) - 1, 0, -1):
        maxpos = 0
        for loc in range(1, fillslot + 1):
            #find the index with highest value
            if num[loc] > num[maxpos]:
                maxpos = loc
            #put them in correct position by swapping
            num[fillslot], num[maxpos] = num[maxpos], num[fillslot]
    return True


def insertionsort_ascending(num):
    """In place insertion sort"""
    for loc in range(1, len(num)):
        # this variable(pos) tracks the index as the item in the list
        # moves back after each comparison
        pos = loc
        # this variable(item) holds the item in the list until
        # it gets the location to be inserted
        item = num[loc]
        inner = True
        while pos > 0 and inner:
            # this if block keeps shifting item forward
            if item < num[pos - 1]:
                #exchange position of items
                num[pos] = num[pos - 1]
                pos = pos - 1
            else:
                # no more comparison needed, the rest
                # of the list is already sorted
                inner = False
        if loc != pos:
            num[pos] = item

    return True


def shellsort_ascending(num):
    """In place shell sort
    """
    gapseq = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gapseq:
        #now it's basically an insertion sort using the gap value
        outer = True
        while gap < len(num) and outer:
            for loc in range(gap, len(num)):
                pos = loc
                item = num[loc]
                inner = True
                while pos > gap - 1 and inner:
                    if item < num[pos - gap]:
                        num[pos] = num[pos - gap]
                        pos = pos - gap
                    else:
                        inner = False
                if loc != pos:
                    num[pos] = item
            outer = False

    return True

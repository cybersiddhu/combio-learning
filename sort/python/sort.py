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
            #put them in correct position
            num[fillslot], num[maxpos] = num[maxpos], num[fillslot]

def bsearch_iterative(list, item, sorted=True):
    """Iterative search, no additional module used.
    In case of unsorted list, it is sorted using the core
    sort function

    list
        The list to be searched

    item
        item for lookup

    sorted=True
        If the given list is sorted, by default it expects a sorted list

    """
    if not sorted:
        list.sort()

    first = 0
    last = len(list) - 1
    found = False
    while first <= last and not found:
        middle = (first + last)//2
        if list[middle] == item:
            found = True
        else:
            if list[middle] > item:
                first = middle + 1
            else:
                last = middle - 1

    return found


def bsearch_recursive(list, item, sorted=True):
    """Search through recursion

    list
        The list to be searched

    item
        item for lookup

    sorted=True
        If the given list is sorted, by default it expects a sorted list

    """

    if not sorted:
        list.sort()

    if not list:
        return False
    else:
        mid = len(list)//2 - 1
        if list[mid] == item:
            return True
        else:
            if list[mid] > item:
                bsearch_recursive(list[mid + 1:], item)
            else:
                bsearch_recursive(list[:mid], item)

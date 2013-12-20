package bsearch

import (
    "sort"
)

func BsearchIterative(list []int, item int) bool {
    first := 0
    last := len(list) - 1
    found := false
    if !sort.IntsAreSorted(list) {
        sort.Ints(list)
    }

    for first <= last && !found {
        middle := (first + last) / 2
        if list[middle] == item {
            found = true
        } else if item > list[middle] {
            first = middle + 1
        } else {
            last = middle - 1
        }
    }
    return found
}

func BsearchRecursive(list []int, item int) bool {
    last := len(list)
    if last == 0 {
        return false
    }
    if !sort.IntsAreSorted(list) {
        sort.Ints(list)
    }
    middle := (0 + last) / 2
    if list[middle] == item {
        return true
    } else if item > list[middle] {
        BsearchRecursive(list[middle+1:], item)
    } else {
        BsearchRecursive(list[:middle-1], item)
    }
    return false
}

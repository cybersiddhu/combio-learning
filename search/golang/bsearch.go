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
    if last == 1 {
        if item == list[0] {
            return true
        } else {
            return false
        }
    }
    if !sort.IntsAreSorted(list) {
        sort.Ints(list)
    }
    middle := (last / 2) - 1
    if item == list[middle] {
        return true
    } else if item > list[middle] {
        return BsearchRecursive(list[middle+1:], item)
    } else {
        return BsearchRecursive(list[:middle], item)
    }
    return false
}

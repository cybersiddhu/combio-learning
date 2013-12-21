package bsearch

import (
    "testing"
)

func TestBsearchIterative(t *testing.T) {
    list := []int{2, 3, 8, 16, 32, 71, 76, 98, 123}
    item := 98
    if !BsearchIterative(list, item) {
        t.Errorf("could not find item %d\n", item)
    }
    if BsearchIterative(list, 24) {
        t.Errorf("should not find item %d\n", 24)
    }
    if !BsearchIterative([]int{29, 22, 54, 32, 12, 9}, 32) {
        t.Error("could not find item in unsorted list")
    }
}

func TestBsearchRecursive(t *testing.T) {
    list := []int{2, 3, 8, 16, 32, 71, 76, 98, 123}
    item := 98
    if !BsearchRecursive(list, item) {
        t.Errorf("could not find item %d\n", item)
    }
    //if !BsearchRecursive([]int{29, 22, 54, 32, 12, 9}, 32) {
    //t.Error("could not find item in unsorted list")
    //}
    //if BsearchRecursive(list, 24) {
    //t.Errorf("should not find item %d\n", 24)
    //}
}

package algorithms

import (
    "testing"
)

func TestMergeSort(t *testing.T) {
    nums := []int{9, 2, 15, 4, 90, 7, 22}
    if !Equal(MergeSort(nums), []int{2, 4, 7, 9, 15, 22, 90}) {
        t.Error("Could not sort slice using mergesort")
    }
}

func TestRaRadixSort(t *testing.T) {
    nums := []int{213, 55, 21, 5, 2334, 31, 430, 20}
    RadixSort(nums)
    if !Equal(nums, []int{5, 20, 21, 31, 55, 213, 430, 2334}) {
        t.Error("Could not sort slice using radixsort")
    }
}

func Equal(left []int, right []int) bool {
    if len(left) != len(right) {
        return false
    }
    for i := range left {
        if left[i] != right[i] {
            return false
        }
    }
    return true
}

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

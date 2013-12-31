//Package algorithms provides functions for sorting integer slices
//using different algorithms
package algorithms

//Mergesort implements mergesort algorithm. It accepts an integer slice
//and then returns its sorted version
func MergeSort(nums []int) []int {
    if len(nums) < 2 {
        return nums
    }
    middle := len(nums) / 2
    left := MergeSort(nums[middle:])
    right := MergeSort(nums[:middle])
    return Merge(left, right)
}

//Merge sorts and merge two already sorted integer slices.
func Merge(left, right []int) []int {
    i, j := 0, 0
    var result []int
    //picks up the minimum element and push it to a new slice
    //Also advances the index pointer
    for i < len(left) && j < len(right) {
        if left[i] < right[j] {
            result = append(result, left[i])
            i += 1
        } else {
            result = append(result, right[j])
            j += 1
        }
    }
    if i < len(left) {
        result = append(result, left[i:]...)
    }
    if j < len(right) {
        result = append(result, right[j:]...)

    }
    return result
}

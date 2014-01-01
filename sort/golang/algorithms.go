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

//RadixSort implements radixsort algorithm, in place sorting of
//of integer slice
func RadixSort(nums []int) {
    base := 10

    //Identify number with most digits
    max := 0
    for _, item := range nums {
        if item > max {
            max = item
        }
    }

    //The loop runs until it reaches maximum position of digit.
    //It is done by dividing the maximum digit number with the decimal
    //numeric power. The power increments by a factor of numeric
    //base(10) on each iteration(1,10,100,1000 etc..)
    for power := 1; max/power > 0; power *= base {
        //Create bucket(a 2d slice) list with 10 bucket, each for one digit
        //in base 10 numeric system
        var bucket [10][]int

        for _, item := range nums {
            //Get the digit value of every number starting
            //from the right(least significant digit)
            digit := int(item / power % base)

            //Place it on a bucket matching its digit value
            bucket[digit] = append(bucket[digit], item)
        }
        //After each pass of sorting based on digit value
        //take them of the bucket and put them back in the original
        //slice
        index := 0
        for i := 0; i < len(bucket); i++ {
            for _, item := range bucket[i] {
                nums[index] = item
                index++
            }

        }

    }

}

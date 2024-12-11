func maximumBeauty(nums []int, k int) int {
    result := 0
	
	sort.Ints(nums)

	l := 0 
	for r  := range nums {
		for nums[r] - nums[l] > 2 * k {
			l++
		}
		result = max(result,r-l+1)
	}
	return result
}
func max(a,b int)int{
	if a > b {
		return a
	}
	return b
}

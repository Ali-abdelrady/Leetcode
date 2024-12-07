func minimumSize(nums []int, maxOperations int) int {
    l , r := 1 , slices.Max(nums)
	for l <= r {
		mid := l + ((r-l)/2)
		if canDivide(mid,maxOperations,nums){
			r = mid - 1
		}else{
			l = mid + 1
		}
	}
	return l
}
func canDivide(maxBalls,maxOperations int, nums []int)bool{
	ops := 0 
	for _,n := range nums {
		ops += int(math.Ceil(float64(n) / float64(maxBalls))) - 1
		if ops > maxOperations {
			return false
		} 
	}
	return true
}

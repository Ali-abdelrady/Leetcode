func maxCount(banned []int, n int, maxSum int) int {
    cnt, sum := 0, 0
	num := 1
	mp := map[int]bool{}

	for _, el := range banned {
		mp[el] = true
	}
	for num <= n {
		if !mp[num] {
			if sum+num <= maxSum {
				cnt++
				sum += num
			} else {
				return cnt
			}
		}
		num++
	}
	return cnt
}
type pair struct {
	first  int
	second int
}
func findScore(nums []int) int64 {
    arr := []pair{}
	var score int64 = 0 

	for index, value := range nums {
		arr = append(arr, pair{index, value})
	}

	sort.Slice(arr,func(i, j int) bool {
		if arr[i].second == arr[j].second {
			return arr[i].first < arr[j].first 
		}
		return arr[i].second < arr[j].second 
	})

	isMarked := map[int]bool{}


	for _ , pair := range arr {
		index , value := pair.first , pair.second
		if !isMarked[index] {
			score += int64(value)
			isMarked[index] = true
			isMarked[index + 1] = true
			isMarked[index - 1] = true
		}
	}
	return score
}
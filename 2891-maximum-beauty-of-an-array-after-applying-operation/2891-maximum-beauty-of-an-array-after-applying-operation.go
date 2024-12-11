type pair struct {
	first int 
	second int
} 
func maximumBeauty(nums []int, k int) int {
    pairs := []pair{}

	for _,num := range nums {
		pairs = append(pairs, pair{num - k , 1})
		pairs = append(pairs, pair{num + k + 1  , -1})
	}
	//sort them based of first element

	sort.Slice(pairs,func(i, j int) bool {
		if pairs[i].first == pairs[j].first {
			return pairs[i].second < pairs[j].second
		}
		return pairs[i].first < pairs[j].first
	})
    fmt.Println(pairs)
	result := 0 
	cnt := 0 

	for _,pair := range pairs{
		cnt += pair.second
		result = max(result , cnt)
	}
	return result
}
func max(a,b int)int{
	if a > b {
		return a
	}
	return b
}

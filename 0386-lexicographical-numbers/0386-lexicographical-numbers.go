func lexicalOrder(n int) []int {
    res := []int{}
	i := 1 
	for  i < 10 && i <= n {
		dfs(i, n, &res)
        i++
	}
    return res
}
func dfs(num, max_num int, res *[]int) {
		if(num > max_num){return}
		*res = append(*res,num)
		for i := 0 ; i < 10 ; i++ {
			child := (num*10) + i
			dfs(child, max_num, res)
		}
}
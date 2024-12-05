func addSpaces(s string, spaces []int) string {
    n := len(s) + len(spaces)
	runes := make([]rune, n)
	i, j := 0, 0

	for index, _ := range runes {
		if j < len(spaces) && spaces[j] == i {
			runes[index] = ' '
			j++
		} else {
			runes[index] = rune(s[i])
			i++
		}
	}
    return string(runes)
	
}
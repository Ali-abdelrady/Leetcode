func canMakeSubsequence(str1 string, str2 string) bool {

    if len(str2) > len(str1){
		return false
	}
    i, j := 0, 0
    
    for i < len(str1) && j < len(str2) {
		if str2[j] == str1[i] || str2[j] == byte(nextChar(rune(str1[i]))) {
			j++
		}
		i++
	}
	if j == len(str2) {
		return true
	}
	return false  
}
func nextChar(ch rune) rune {
	if ch == 'z' {
		return 'a'
	}
	return ch + 1
}

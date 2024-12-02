func isPrefixOfWord(sentence string, searchWord string) int {
    words := strings.Split(sentence, " ")

	for i,word := range words {
		if len(word) >= len(searchWord) && isPrefix(word,searchWord){
			return i + 1 
		}
	}
	return -1
}
func isPrefix(word,prefix string)bool{
	i , j := 0 , len(prefix)

    if word[i:j] == prefix {
		return true
	}
	// for j < len(word){
	// 	if word[i:j] == prefix {
	// 		return true
	// 	}
	// 	j++
	// 	i++
	// } 
	return false
}
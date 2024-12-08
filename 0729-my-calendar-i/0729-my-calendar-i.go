type tree struct {
	left  *tree
	right *tree
	start int
	end   int
}

func (t *tree) insert(start, end int) bool {
	curNode := t
	for {
		if start >= curNode.end {
			if curNode.right == nil {
				curNode.right = &tree{start: start, end: end}
				return true
			}
			curNode = curNode.right
		} else if end <= curNode.start {
			if curNode.left == nil {
				curNode.left = &tree{start: start, end: end}
				return true
			}
			curNode = curNode.left
		} else {
			return false
		}
	}
}

type MyCalendar struct {
	root *tree
}

func Constructor() MyCalendar {
	return MyCalendar{root: nil}
}

func (this *MyCalendar) Book(startTime int, endTime int) bool {
    if this.root == nil {
		this.root = &tree{start: startTime, end: endTime}
		return true
	}
	return this.root.insert(startTime, endTime)
}


/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(startTime,endTime);
 */
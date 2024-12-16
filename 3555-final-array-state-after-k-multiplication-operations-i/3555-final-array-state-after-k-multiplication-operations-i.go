type pair struct {
	value  int
	index int
}

// MinHeap represents a max-heap
type MinHeap []pair

func (h MinHeap) Len() int { return len(h) }

func (h MinHeap) Less(i, j int) bool { 
	if h[i].value == h[j].value {
		return h[i].index < h[j].index
	}
	return h[i].value < h[j].value 
}

func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x any) {
	*h = append(*h, x.(pair))
}

func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
func getFinalState(nums []int, k int, multiplier int) []int {
    pq := &MinHeap{}
	heap.Init(pq)

	//Push all array element to the heap
	for index,value := range nums {
		heap.Push(pq,pair{value,index})
	}

	// 
	for k > 0 {
		//Get the top of the heap
		min := heap.Pop(pq).(pair)
		
		// Update the mini index in array
		nums[min.index] *= multiplier

		// Push the updated element to the heap
		heap.Push(pq,pair{nums[min.index] , min.index})
		k--
	}
	fmt.Println(nums)
    return nums
}
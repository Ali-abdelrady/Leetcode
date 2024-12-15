type pair struct {
	value  float64
	index int
}

// MaxHeap represents a max-heap
type MaxHeap []pair

// Len is part of heap.Interface
func (h MaxHeap) Len() int { return len(h) }

// Less is part of heap.Interface (reversed for max-heap)
func (h MaxHeap) Less(i, j int) bool { return h[i].value > h[j].value }

// Swap is part of heap.Interface
func (h MaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

// Push adds an element to the heap
func (h *MaxHeap) Push(x any) {
	*h = append(*h, x.(pair))
}

// Pop removes and returns the maximum element
func (h *MaxHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
func maxAverageRatio(classes [][]int, extraStudents int) float64 {
    pq := &MaxHeap{}
	heap.Init(pq)

	for index := range classes {
		heapPush(classes,index,pq)
	}

	for extraStudents > 0 {
		// Get the top from max heap 
		max := heap.Pop(pq).(pair)

		//update the classe with maxAvg
		classes[max.index][0]++
		classes[max.index][1]++

		// Push the upadted classes to the heap again 
		heapPush(classes,max.index,pq)
		extraStudents -- 
	}

	//Calculate max Average

	sum := 0.0
	for _ , class := range classes {
		pass , total := class[0] , class[1]
		sum += float64 (pass) / float64(total) 
	}

	return sum / float64(len(classes))
}
func heapPush(classes[][]int,index int ,pq *MaxHeap ){
	pass , total := classes[index][0] , classes[index][1]
	currRatio := float64 (pass) / float64(total) 
		newRatio := float64 (pass + 1) / float64(total + 1 )
		diff := newRatio - currRatio
		heap.Push(pq,pair{diff,index})
}
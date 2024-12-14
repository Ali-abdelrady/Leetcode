func continuousSubarrays(nums []int) int64 {
    var ans int64
    maxNum := nums[0]
    minNum := nums[0]

    for left, right := 0, 0; right < len(nums); right++ {
        if abs(nums[right] - maxNum) <= 2 && abs(nums[right] - minNum) <= 2 {
            ans += int64(right - left + 1)
            maxNum = max(maxNum, nums[right])
            minNum = min(minNum, nums[right])
            continue
        }

        maxNum = nums[right]
        minNum = nums[right]
        for j := right; j >= left; j-- {
            if abs(nums[right] - nums[j]) > 2 {
                left = j+1
                break
            }
            maxNum = max(maxNum, nums[j])
            minNum = min(minNum, nums[j])
        }
        ans += int64(right - left + 1)
    }
    return ans
}

func abs(num int) int {
    if num < 0 {
        return -num
    }
    return num
}
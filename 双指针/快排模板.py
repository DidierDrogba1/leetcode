#快排先整体有序，再局部有序。 
#先让[start, right] & [left, end]有序
#(左边>= pivot，右边 < pivot), 之后再让两个区间局部有序

def quickSort(self, nums):
	if not nums:
		return nums 
	self.quickSortHelper(nums, 0, len(nums) - 1)


def quickSortHelper(self, nums, start, end):
	if start >= end:
		return 
	pivot = nums[start + (end - start) // 2]
	left, right = start, end 

	while left <= right:
		while left <= right and nums[left] < pivot:
			left += 1
		while left <= right and nums[right] > pivot: #注意nums[right] == pivot时候，R指针停止，等待交换
			right -= 1
		if left <= right: #互换 只能用if，因为只判断一次，结束后立马返回第一个while；不然会一直互换
			nums[left], nums[right] == nums[right], nums[left]
			left += 1
			right -= 1

	self.quickSortHelper(nums, start, right)
	self.quickSortHelper(nums, left, end)





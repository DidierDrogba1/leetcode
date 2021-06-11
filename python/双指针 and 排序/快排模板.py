#快排先整体有序，再局部有序。 
#先让[start, right_pointer] & [left_pointer, end]有序
#(左边>= pivot，右边 <= pivot), 之后再让两个区间局部有序


#快速排序在大部分时候的时间复杂度都是O(nlogn)，
#但是当数组为逆序排序时（假设每次以第一个元素为pivot），时间复杂度将会退化到O(n^2)
#快排空间复杂度: 堆空间为0, 没有使用额外空间，都是在原数组上操作；栈空间为递归深度，平均为O(logn)



def quickSort(self, nums):
	if not nums:
		return nums 
	self.quickSortHelper(nums, 0, len(nums) - 1)


def quickSortHelper(self, nums, start, end):
	if start >= end:
		return 
	pivot = nums[start + (end - start) // 2]
	left_pointer, right_pointer = start, end 

	while left_pointer <= right_pointer:
		while left_pointer <= right_pointer and nums[left_pointer] < pivot: #注意这里是while，而且没有等号
			left_pointer += 1
		while left_pointer <= right_pointer and nums[right_pointer] > pivot: #注意nums[right_pointer] == pivot时候，R指针停止，等待交换
			right_pointer -= 1
		if left_pointer <= right_pointer: #互换 只能用if，因为只判断一次，结束后立马返回第一个while；不然会一直互换
			nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
			left_pointer += 1
			right_pointer -= 1

	self.quickSortHelper(nums, start, right_pointer) #先整体有序，再局部有序
	self.quickSortHelper(nums, left_pointer, end)





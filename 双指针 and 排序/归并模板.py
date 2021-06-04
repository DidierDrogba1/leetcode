#归并排序，先局部有序，在整体有序
#归并排序使用了分治的思想，无论是什么样的数据，所花费的时间都是O(nlogn)的。
#空间复杂度： 堆空间为O(n),因为声明了一个tmp ； 栈空间为递归深度，即O(h) = O(logn), 可以看作一颗平衡二叉树
def mergeSort(self, nums):
	tmp = [0 for _ in range(len(nums))]
	self.mergeSortHelper(nums, tmp, 0, len(nums) - 1)

def mergeSortHelper(self, nums, tmp, start, end): #注意都要带着tmp这个参数
	if start >= end:
		return
	mid = start + (end - start) // 2
	self.mergeSortHelper(nums, tmp, start, mid) #注意都要带着tmp这个参数
	self.mergeSortHelper(nums, tmp, mid + 1, end)
	self.merge(nums, tmp, start, end, mid)

def merge(self, nums, tmp, start, end, mid):
	left_pointer, right_pointer = start, mid + 1
	tmp_index = start

	while left_pointer <= mid and right_pointer <= end:
		if nums[left_pointer] <= nums[right_pointer]:
			tmp[tmp_index] = nums[left_pointer]
			left_pointer += 1
			tmp_index += 1
		else:
			tmp[tmp_index] = nums[right_pointer]
			right_pointer += 1
			tmp_index += 1


	while left_pointer <= mid:
		tmp[tmp_index] = nums[left_pointer]
		left_pointer += 1
		tmp_index += 1		
	while right_pointer <= end:
		tmp[tmp_index] = nums[right_pointer]
		right_pointer += 1			
		tmp_index += 1

	for i in range(start, end + 1):
		nums[i] = tmp[i]







	


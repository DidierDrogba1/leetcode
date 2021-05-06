#归并排序，先局部有序，在整体有序
def mergeSort(self, nums):
	tmp = [0 for _ in range(len(nums))]
	self.mergeSortHelper(nums, tmp, 0, len(nums) - 1)




def mergeSortHelper(self, nums, tmp, start, end):
	if start >= end:
		return
	mid = start + (end - start) // 2
	self.mergeSortHelper(nums, tmp, start, mid)
	self.mergeSortHelper(nums, tmp, mid + 1, end)
	self.merge(nums, tmp, start, end, mid)

def merge(self, nums, tmp, start, end, mid):
	start, mid + 1 = left, right 
	tmp_index = start

	while left <= mid and right <= end:
		if nums[left] <= nums[right]:
			tmp[tmp_index] = nums[left]
			left += 1
			tmp_index += 1
		else:
			tmp[tmp_index] = nums[right]
			right += 1
			tmp_index += 1


	while left <= mid:
		tmp[tmp_index] = nums[left]
		left += 1
		tmp_index += 1		
	while right <= end:
		tmp[tmp_index] = nums[right]
		right += 1			
		tmp_index += 1

	for i in range(start, end + 1):
		nums[i] = tmp[i]







	


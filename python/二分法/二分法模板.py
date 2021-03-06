#二分法是在排好序的数组上进行
def binarySearch(self, nums, target):
	if not nums:
		return -1

	start, end = 0, len(nums) - 1

	## 切记，这里是 s+1<e
	while start + 1 < end:
		mid = (start + end) // 2

		if nums[mid] < target:
			start = mid 
		elif nums[mid] == target: # 此情况为找first index；如果找最后一个index，这里就应该是 start = mid 
			end = mid 
		else:
			end = mid 
 	#如果找第一个就先start，如果找最后一个就先看end
	if nums[start] == target:
		return start 
	if nums[end] == target:
		return end
	return -1 

## 递归方式实现二分法
def binarySearch(self, nums, target):
	if not nums:
		return -1



def binarySearch_Helper(self, nums, target, start, end):
	if start + 1 >= end:
		if nums[start] == target:
			return start 
		if nums[end] == target:
			return end
		return -1 

	mid = start + (end - start) // 2 
	tmp = nums[mid]
	if tmp < target:
		return self.binarySearch_Helper(nums, target, mid, end)
	elif tmp > target:
		return self.binarySearch_Helper(nums, target, start, mid)
	elif tmp == target: 
		return self.binarySearch_Helper(nums, target, mid, end)



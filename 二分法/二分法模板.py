def binarySearch(self, nums, target):
	if not nums:
		return -1

	start, end = 0, len(nums) - 1

	while start + 1 < end:
		mid = (start + end) // 2

		if nums[mid] < target:
			start = mid 
		# elif nums[mid] == target:
		# 	end = mid 
		else:
			end = mid 
 	#如果找第一个就先start，如果找最后一个就先看end
	if nums[start] == target:
		return start 
	if nums[end] == target:
		return end
	return -1 
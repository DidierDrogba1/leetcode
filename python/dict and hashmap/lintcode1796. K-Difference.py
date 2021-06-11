class Solution:
    """
    @param nums: a integer array
    @param target: 
    @return: return a integer
    """
    def KDifference(self, nums, target):
        # write your code here
        if not nums:
            return 0
        s = set()
        cnt = 0
        for num in nums:
            if num + target in s:
                cnt += 1
            if num - target in s:
                cnt += 1
            s.add(num)
        return cnt 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        currentSum = 0
        maxSum = float('-inf')
        for x in nums:
            currentSum += x
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum < 0:
                currentSum = 0
        return maxSum
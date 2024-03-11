class Solution(object):
    
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1]*len(nums)
        post =  1
        pre =  1
        for i in range(0,len(nums)):
            answer[-1-i] *= post
            answer[i] *= pre
            pre *= nums[i]
            post *= nums[-1-i]

			
        return answer
    

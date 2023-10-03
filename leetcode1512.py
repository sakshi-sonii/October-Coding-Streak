from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(i<j and nums[i]==nums[j]):
                    count+=1
        return count
    
solution = Solution()
ans = solution.numIdenticalPairs([1,2,3,1,1,3])
print(ans)
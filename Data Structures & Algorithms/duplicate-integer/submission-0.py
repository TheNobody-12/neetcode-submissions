class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        # O(n2) and O(1) 

        # sorting takes O(nlogn) space O(1) or O(n)
        # nums.sort()
        # for i range(1 , len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False

        # Hash Set
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False




        
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = 1 + seen.get(num,0)
        
        arr = []
        for num,cnt in seen.items():
            arr.append([cnt,num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res



        
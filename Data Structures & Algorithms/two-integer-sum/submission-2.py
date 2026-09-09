class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(0, len(nums)):
            store[target-nums[i]] = i
        for i in range(0, len(nums)):
            if nums[i] in store.keys() and store.get(nums[i]) != i:
                return [i, store.get(nums[i])]
        return []
        

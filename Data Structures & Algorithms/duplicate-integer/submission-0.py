class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use Hash table to find the duplicate values.
        # since we have dictionary in python we can use that.
        hashtable = dict()
        result = False
        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                result = True
                break
        return result
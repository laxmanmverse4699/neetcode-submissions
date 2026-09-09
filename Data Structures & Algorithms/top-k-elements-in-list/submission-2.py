class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for num in nums:
            if num in store:
                store[num] = store.get(num) + 1
            else:
                store[num] = 1
        sorted_freq = dict(sorted(store.items(), key=lambda x: x[1], reverse=True))  
        result = []
        i = 0
        for key, value in sorted_freq.items():
            if i < k:
                result.append(key)
                i += 1
        return result

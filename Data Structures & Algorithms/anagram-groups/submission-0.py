class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        store = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in store:
                temp_list = store.get(sorted_str)
                temp_list.append(str)
            else:
                store[sorted_str] = [str]
        result = []
        for key in store:
            result.append(store.get(key))
        return result
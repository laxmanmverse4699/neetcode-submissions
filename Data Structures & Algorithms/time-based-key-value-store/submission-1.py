class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        result = self.store.get(key, [])
        left, right = 0, len(result) - 1
        output_res = ""

        while left <= right:
            mid = (left + right) // 2
            value, timestamp_pre = result[mid]
            
            if timestamp_pre <= timestamp:
                output_res = value
                left = mid + 1  
            else:
                right = mid - 1  

        return output_res

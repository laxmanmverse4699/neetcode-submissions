class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> list = new HashMap<>();
        for(int i=0 ; i < nums.length; i++) {
            // each interger are unique.
            list.put(target-nums[i], i);
        }
        int[] result = new int[2];
        for(int i = 0 ; i < nums.length ; i++) {
            if(list.containsKey(nums[i]) && list.get(nums[i]) != i) {
                result[0] = i;
                result[1] = list.get(nums[i]);
                return result;
            }
        }
        return new int[2];
    }
}

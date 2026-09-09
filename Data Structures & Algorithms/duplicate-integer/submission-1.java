
class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> dup = new HashSet<>();
        Boolean result = false;
        for( int i: nums) {
            if(dup.contains(i)){
                result = true;
                break;
            } else {
                dup.add(i);
            }
        }
        return result;
    }
}
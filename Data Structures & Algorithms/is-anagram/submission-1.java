class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        HashMap<Character, Integer> store = new HashMap<>();

        for(char key : s.toCharArray()) {
            if(store.containsKey(key)) {
                store.put(key, store.get(key)+1);
            } else{
                store.put(key, 1);
            }
        }
        // for second string we need to find all the characters are same or not.
        for(char key : t.toCharArray()) {
            if(store.containsKey(key)) {
                store.put(key, store.get(key)-1);
            } else{
                return false;
            }
        }
        for(int val : store.values()) {
            if(val > 0){
                return false;
            }
        }
        return true;
    }
}

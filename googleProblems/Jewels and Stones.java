import java.util.HashSet;

class Solution {
    public int numJewelsInStones(String J, String S) {
        int num_jewels = 0;
        HashSet<Character> set = new HashSet<Character>();
        // Add J to a hashset of characters
        for (int i = 0; i < J.length(); i++) {
            set.add(J.charAt(i));
        }

        // Go through set and see if the indexed stone is 
        // a jewel
        for (int i = 0; i < S.length(); i++) {
            if (set.contains(S.charAt(i))) num_jewels++;
        }
        return num_jewels;
    }
}
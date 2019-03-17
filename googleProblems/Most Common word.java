import java.util.HashSet;
class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        // Split paragraph into a string of words
        String[] words = paragraph.split("\\W+");
        int count = 0;
        String temp = "";

        // Create a HashSet
        HashSet<String> set_of_words = new HashSet<String>();

        HashSet<String> set_of_banned_words = new HashSet<String>();
        
        // add all banned words to a set
        for (int i = 0; i < banned.length; i++) set_of_banned_words.add(banned[i]);

        for (int i = 0; i < words.length; i++) {
            // If the set contains the word already
            // increment the count
            if (set_of_words.contains(words[i]) && !set_of_banned_words.contains(words[i]))
            {
                temp = words[i];
                count++;
            }
            else if (!set_of_words.contains(words[i])){
                count = 0;
                set_of_words.add(words[i]);
            }
            System.out.println("Current word: " + words[i] + ", Temp is: " + temp);
        }
        return temp;
    }
}
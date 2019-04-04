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
            words[i] = words[i].toLowerCase(); // Convert to lower case
            
            // If the word is part of the set of valid words
            if (!set_of_banned_words.contains(words[i]))
            {
                set_of_words.add(words[i]);
                System.out.println("Note: Adding '" + words[i] + "' to the set\n");
                if (set_of_words.contains(words[i]))
                {
                    // Set temporary word as result
                    temp = words[i];
                    count++;
                }
                // Reset count and add to set
                count = 0;
            }
        }
        System.out.println("TEmp is: " + temp);
        return (set_of_words.contains(temp)) ? temp: words[0].toLowerCase() ;
    }
}
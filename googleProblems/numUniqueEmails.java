class Solution {
    public int numUniqueEmails(String[] emails) {
        HashSet<String> set = new HashSet<>();
        
        for (String email: emails) {            
            StringBuilder clean_email = new StringBuilder();
            // For every email in emails array, clean it up
            // by dealing with the . and + 
            for (int j = 0; j < email.length(); j++) {
                char c = email.charAt(j);
                if (c == '.') {
                    continue;
                }
                else if (c == '+' || c == '@') {
                    // Skip through all char until we 
                    // hit a '@' symbol
                    while (email.charAt(j) != '@') {
                        j++;
                    }

                    // Append @blah.com to string
                    clean_email.append(email.substring(j));
                    break;
                }
                else {
                    clean_email.append(c);
                }                
            }
            System.out.println("old email: " + email + "\nnew email: " + clean_email);
            // Add all unique addresses to hashset
            set.add(clean_email.toString());
            
         }
        return set.size();
    }
}
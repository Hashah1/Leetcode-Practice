class Solution {
    public boolean isPalindrome(int x) {
        // convert integer to string
        String x_in_string = Integer.toString(x);

        // Set an index which will start
        // from end of string and decrement
        // every iteration
        int j = x_in_string.length() - 1;
        
        for (int i = 0; i < j; i++)
        {
            // If each index of array is different from the end,
            // return false.
            if (x_in_string.charAt(i) != x_in_string.charAt(j))
                return false;
            j--; 
        }
        return true;
    }
}
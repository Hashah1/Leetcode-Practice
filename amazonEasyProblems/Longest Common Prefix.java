import java.util.*;
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String result = "";
        int individual_str_count = 0;
        Arrays.sort(strs); // sort array

        for (int index = 0; index < strs.length - 1; index++)
        {

            // Check if the next string to compare is shorter than current one
            // if it is, loop until the end
            if (strs[index+1].length() < strs[index].length())
            {
                individual_str_count =  strs[index+1].length();
            }
            else 
            {
            individual_str_count =  strs[index].length();
            }

            for (int individual_str_index = 0; individual_str_index < individual_str_count; individual_str_index++)
            {
                if (strs[index].charAt(individual_str_index) == strs[index+1].charAt(individual_str_index))
                {
                    // if (strs[index].charAt(individual_str_index) == result.charAt(individual_str_index))
                    // {
                    //     break;
                    // }
                    // else
                        result += strs[index].charAt(individual_str_index);
                }
            }
            
        }
        return result;
    }
}
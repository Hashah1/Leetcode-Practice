import java.util.*;

/* 
Solution 1: Brute Force
*/
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Error checking in case an empty array 
        // is passed
        if (nums == null){
            return new int[] {-1,-1};
        }

        // Loop through each element in
        // array twice.
        for (int num_1 = 0; num_1 < nums.length; num_1++) {
            for (int num_2 = num_1 + 1; num_2 < nums.length; num_2++) {
                // Check to see if the sum is equal to target
                 if ((nums[num_1] + nums[num_2]) == target)
                     // Store the indices in array
                     return new int[] { num_1, num_2 };
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}

/**
 * Solution 2: One-pass hash map
 */

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Declare HashMap
        Map<Integer, Integer> map = new HashMap<>();

        
        // Loop through each element in
        // array twice.
        for (int num = 0; num < nums.length; num++) {
            if (map.containsKey(target - nums[num]))
                return new int[]{map.get(complement), num};
            map.put(nums[num], num);

        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
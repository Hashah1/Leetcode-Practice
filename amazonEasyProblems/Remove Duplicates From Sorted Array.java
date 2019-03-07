class Solution {
    public int removeDuplicates(int[] nums) {
        int total_length = nums.length;
        int j;
        if (total_length == 0)
        {
            return total_length;
        }

        for (int i = 0; i < nums.length - 1; i++)
        {
            j = i + 1;

            if (nums[i] == nums[j])
            {
                nums[i] = nums[j];
                total_length--;
            }
        }
        return total_length;
    }
}
class Solution {
    public int rob(int[] nums) {
        int total1 = 0;
        int total2 = 0;
        int j = nums.length;
        for (int i = 0; i < nums.length; i += 2) {
            total1 += nums[i];
            total2 += nums[j];
            j -= 2;
        }

        return Math.max(total1, total2);
    }
}
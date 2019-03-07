/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        int middle_element = nums.length/2; // get the middle value of array
        
        TreeNode node = new TreeNode(middle_element);
        
    }
}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
        Thought Process:
        TC: O(len(nums) * len(subarray))
        SC: O(len(nums))

        - root = Pick the max from nums, and thats going to be the root
        - root.left = Pass left_bound..root_idx - 1 to the next recursion_call
        - root.right = Pass root_idx + 1..right_bound to the next recursion_call
        Bottleneck issue: Max value
        """
        def helper(left, right):
            if left > right:
                return None
            max_val, max_val_idx = get_max(left, right)
            root = TreeNode(max_val)
            root.left = helper(left, max_val_idx - 1)
            root.right = helper(max_val_idx + 1, right)
            return root

        def get_max(left, right):
            max_val, max_idx = 0, 0
            for idx in range(left, right + 1):
                val = nums[idx]
                if val >= max_val:
                    max_val = val
                    max_idx = idx
            return max_val, max_idx

        return helper(0, len(nums) - 1)
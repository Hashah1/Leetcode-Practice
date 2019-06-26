def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root: 
            # if node has right subtree, find min of right subtree
            if p.right:
                root = p.right
                while root.left:
                    root = root.left
                    print("here: " + str(root.val))
            else:  # Node is in left subtree.
                parent = None
                while root != p:
                    if p.val < root.val:
                        parent = root
                        root = root.left
                    else:
                        root = root.right
                return parent
        return root
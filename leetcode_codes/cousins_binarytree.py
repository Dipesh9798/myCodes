# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSibling(self,root,x,y):
        if not root:
            return False
        a=False
        b=False
        if (root.left and root.right):
            a=(root.left.val==x)and(root.right.val==y)
            b=(root.left.val==y)and(root.right.val==x)
        c=self.isSibling(root.left,x,y)
        d=self.isSibling(root.right,x,y)
        return a or b or c or d
    def depth(self,root,x,d):
        if root==None:
            return 0
        if root.val==x:
            return d
        l=self.depth(root.left,x,d+1)
        if (l!=0):
            return 1
        return self.depth(root.right,x,d+1)
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if((self.depth(root,x,1)==self.depth(root,y,1)) and (not self.isSibling(root,x,y))):
            return True
        else:
            return False


###############################################################################
#                                ANOTHER METHOD                               #
###############################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent = {root.val : 0}
        label = {root.val : 1}
        def setParent(root, l):
            if not root:
                return
            if root.left:
                parent[root.left.val] = root.val
                label[root.left.val] = l + 1
                setParent(root.left, l + 1)
            if root.right:
                parent[root.right.val] = root.val
                label[root.right.val] = l + 1
                setParent(root.right, l + 1)
        setParent(root, 1)
        return parent[x] != parent[y] and label[x] == label[y]



        
        

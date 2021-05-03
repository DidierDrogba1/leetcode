# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.ans = None

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        # height
        h = self.__getHeight(root)
        # width, 2^h - 1
        w = (1<<h) -1
        self.ans = [["" for i in range(w)] for j in range(h)]
        self.__fill(root,self.ans,0,0,w-1)
        return self.ans

    def __getHeight(self, root):
        if not root:
            return 0
        return max(self.__getHeight(root.left),self.__getHeight(root.right)) + 1

    def __fill(self, root, ans, h, l, r):
        if not root:
            return
        mid = (l + r) / 2
        ans[h][mid] = str(root.val)
        # fill left subtree
        self.__fill(root.left,ans,h+1,l,mid-1)
        # fill right subtree
        self.__fill(root.right,ans,h+1,mid+1,r)

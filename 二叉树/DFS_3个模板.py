def preorderTraversal(self, root: TreeNode) -> List[int]:
	res = []
	self.helper(root)
	return res 

def helper(self, node, res):
	if not root:
		return 
	res.append(node.val)
	self.helper(node.left, res)
	self.helper(node.right, res)

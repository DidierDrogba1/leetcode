class BST_solution:
	
	def add_helper(self, root, val):
		if not root:
			return TreeNode(val)
		if val < root.val:
			root.left = self.add_helper(root.left, val)
		if val > root.val:
			root.right = self.add_helper(root.right, val)

		return root 

	def contain_helper(self, root, val):
		if not root:
			return False 

		if val == root.val:
			return True 
		elif val < root.val:
			self.contain_helper(root.left, val)
		elif val > root.val:
			self.contain_helper(root.right, val)			
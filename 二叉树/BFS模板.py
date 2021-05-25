#BFS普通实现
def BFS(self, root):
	if not root:
		return []
	final_ans = []
	queue = collections.deque()
	queue.append(root)

	while queue:
		tmp_element = queue.popleft()
		final_ans.append(tmp_element.val)
		if tmp_element.left:
			queue.append(tmp_element.left)
		if tmp_element.right:
			queue.append(tmp_element.right)

	return final_ans

#BFS 分层实现
def BFS(self, root):
	if not root:
		return []
	final_ans = []
	queue = collections.deque()
	queue.append(root)

	while queue:
		cur_level_size = len(queue)
		tmp_level_ans = []
		for i in range(cur_level_size):
			tmp_element = queue.popleft()
			tmp_level_ans.append(tmp_element.val)

			if tmp_element.left:
				queue.append(tmp_element.left)
			if tmp_element.right:
				queue.append(tmp_element.right)

		final_ans.append(tmp_level_ans)

	return final_ans




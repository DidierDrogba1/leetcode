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

#   level = 1
	while queue:
		cur_level_size = len(queue)
		tmp_level_ans = []
#		print ('level: ', level)
		for i in range(cur_level_size):
			tmp_element = queue.popleft()
			tmp_level_ans.append(tmp_element.val)

			if tmp_element.left:
				queue.append(tmp_element.left)
			if tmp_element.right:
				queue.append(tmp_element.right)

		final_ans.append(tmp_level_ans)
		#level += 1

	return final_ans


## 双队列做法
    # def BFS(self, root):
    #     if not root:
    #         return 
    #     final_ans = []
    #     queue = collections.deque()
    #     queue.append(root)

    #     while queue:
    #         next_queue = collections.deque()        
    #         tmp_ans = []
    #         #tmp_element = queue.popleft()
    #         for node in queue:
    #             tmp_ans.append(node.val)
    #         for node in queue:     
    #             if node.left:
    #                 next_queue.append(node.left)
    #             if node.right:
    #                 next_queue.append(node.right)  

    #         final_ans.append(tmp_ans)      
    #         queue = next_queue
        
    #     return final_ans 

## dummyNode做法
    # def BFS(self, root):
    #     if not root:
    #         return 
    #     queue = collections.deque()
    #     queue.append(root)
    #     queue.append(None)
    #     final_ans = []
    #     tmp_level_ans = []
    #     while queue:
    #         tmp_element = queue.popleft()
    #         if not tmp_element:
    #             final_ans.append(tmp_level_ans)
    #             tmp_level_ans = []
    #             if queue:
    #                 queue.append(None)
    #             continue 

    #         tmp_level_ans.append(tmp_element.val)
    #         if tmp_element.left:
    #             queue.append(tmp_element.left)
    #         if tmp_element.right:
    #             queue.append(tmp_element.right)
    #     return final_ans

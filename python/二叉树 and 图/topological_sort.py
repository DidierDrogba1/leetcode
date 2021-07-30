# 输入: prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# 输出: [0,1,2,3] or [0,2,1,3]
# 解释:总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。
# 并且课程 1 和课程 2 都应该排在课程 0 之后。
# 因此，一个正确的课程顺序是 [0,1,2,3] 。
# 另一个正确的排序是[0,2,1,3] 。

def findOrder(self, prerequisites):
	# corner case 
	graph = self.build_graph(prerequisites)
	indegree = self.get_indegree(graph)
	topo_order = self.topological_sort(graph)
	return topo_order

def build_graph(self, prerequisites):
	graph = dict()
	# initialization
	for node_list in prerequisites:
		for node in node_list:
			if node not in graph:
				graph[node] = set()
	
	# projection = before_node : after_node
	for node_list in prerequisites:
		for after_node, before_node in node_list:
			graph[before_node].add(after_node)

	return graph

def get_indegree(self, graph):
	# initialization
	indegree = dict()
	for node in graph:
		if node not in indegree:
			indegree[node] = 0

	for before_node in graph:
		neighbors = graph[before_node]:
		for neighbor in neighbors:
			indegree[neighbor] += 1

	return indegree

def topological_sort(self, graph, indegree):
	queue = collections.deque()
	for node in indegree:
		if indegree[node] == 0:
			queue.append(node)

	topo_order = []
	while queue:
		curr_node = queue.popleft()
		topo_order.append(curr_node)
		neighbors = graph[curr_node]
		for neighbor in neighbors:
			indegree[neighbor] -= 1
			if indegree[neighbor] == 0:
				queue.append(neighbor)

	return topo_order

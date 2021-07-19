
class UndirectedGraphNode
     def __init__(self, x)
         self.label = x
         self.neighbors = []


class Solution
    
    @param node A undirected graph node
    @return A undirected graph node
    
    def cloneGraph(self, node)
        # write your code here
        # corner case 
        if not node
            return None
        
        nodes = self.find_nodes_by_bfs(node)
        mapping = self.copy_nodes(nodes)
        self.copy_edges(nodes, mapping)
        return mapping[node]


    def find_nodes_by_bfs(self, node)
        queue = collections.deque([node])
        visited = set([node])
        # visited用来保存所有点
        while queue
            cur_node = queue.popleft()
            for neighbor in cur_node.neighbors
                if neighbor in visited
                    continue 
                else
                    queue.append(neighbor)
                    visited.add(neighbor)
        return list(visited) 

    def copy_nodes(self, nodes)
        mapping = dict()
        #映射关系 旧-新
        for node in nodes
            mapping[node] = UndirectedGraphNode(node.label)
        return mapping 

    def copy_edges(self, nodes, mapping)
        for node in nodes
            # 从dict中找到新node
            new_node = mapping[node]
            for neighbor in node.neighbors
                # 旧点有哪些旧邻居，新点有哪些新邻居
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

    

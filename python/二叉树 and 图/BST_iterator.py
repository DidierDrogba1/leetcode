## solution 1 : stack中记录所有路径
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        ## 初始化，根和根的所有左儿子入栈
        self.find_most_left(root)

    def find_most_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left 

    def next(self) -> int:
        cur_node = self.stack[-1]
        tmp_node = cur_node.right 
        ##有右儿子，把右儿子所有左儿子入栈
        if tmp_node:
            self.find_most_left(tmp_node)
        ## 没有右儿子
        else:
            tmp_node = self.stack.pop()
            ## 如果栈顶元素的右儿子是tmp_node,代表栈顶已经遍历过，出栈。
            ## 因为目前节点已经存到cur_node里面，之后return就行。
            while self.stack and self.stack[-1].right == tmp_node:
                tmp_node = self.stack.pop()
        return cur_node.val 
                
    def hasNext(self) -> bool:
        return len(self.stack) > 0



## solution 2 : stack中不记录所有路径 

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        ## 初始化，根和根的所有左儿子入栈
        self.find_most_left(root)

    def find_most_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left 

    def next(self) -> int:
        ##出栈，如果栈顶元素有右儿子，把右儿子的所有左儿子入栈
        cur_node = self.stack.pop()
        tmp_node = cur_node.right 
        self.find_most_left(tmp_node)
        return cur_node.val 

    def hasNext(self) -> bool:
        return len(self.stack) > 0

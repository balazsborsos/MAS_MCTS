import random
import numpy as np

# Globally tunable parameters
random.seed = 42
C = 2.0  
ROOT_ITER = 50 
ROLLOUT = 5
DEPTH = 12

# creating the structure

class Tree:
    def __init__(self, depth):
        self.depth = depth
        self.tree = self.construct_tree()
        self.leaves = [np.random.uniform(100) for index in range(2 ** (depth))]
    def __str__(self):
        return f'Depth: {self.depth}\nNumber of leafnodes: {2**DEPTH}'

    
    def construct_tree(self):
        tree = []
        for depth in range(DEPTH):
            nodes: list = [Node(depth, index) for index, _ in enumerate(range(2 ** (depth + 1) ))]
            tree.append(nodes)
        for depth in tree:
            for node in depth:
                if node.depth < DEPTH - 1:
                    node.left_child = tree[node.depth + 1][node.index * 2]
                    node.right_child = tree[node.depth + 1][(node.index * 2) + 1]

        return tree
    
class Node:
    def __init__(self, depth, index):
        self.index = index
        self.depth = depth
        self.value = 0.0
        self.num_visits = 0
        self.parent_visits = 0
        self.left_child = None
        self.rith_child = None

    def __str__(self):
        return str(self.depth) + ' ' + str(self.index) + ' ' + str(self.value) + ' ' + str(self.num_visits) + ' ' + str(self.parent_visits)

    def compute_ucb(self):
        return (self.value / self.num_visits) + (C * np.sqrt((np.log(self.parent_visits) / self.num_visits))) if self.num_visits != 0 else 'Infinity'


def selection(node : Node):

    left_child_ucb = node.left_child.compute_ucb()
    right_child_ucb = node.right_child.compute_ucb()

    # Error handling in case visits == 0
    if type(left_child_ucb) == str:
        return node.left_child

    if type(right_child_ucb) == str:
        return node.right_child

    # If node already visited  -> return child with highest UCB
    return node.left_child if left_child_ucb > right_child_ucb else node.right_child

def expansion():

    pass

def simulation():

    pass

def backpropagation():

    pass



if __name__ == '__main__':
    myTree = Tree(DEPTH)
    print(selection(myTree.tree[0][0]))
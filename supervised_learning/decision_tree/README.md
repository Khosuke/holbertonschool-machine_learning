# Project Decision Tree & Random Forest

We will progressively add methods in the following 3 classes :

```
class Node:
    def __init__(self, feature=None, threshold=None, left_child=None, right_child=None, is_root=False, depth=0):
        self.feature                  = feature
        self.threshold                = threshold
        self.left_child               = left_child
        self.right_child              = right_child
        self.is_leaf                  = False
        self.is_root                  = is_root
        self.sub_population           = None    
        self.depth                    = depth

class Leaf(Node):
    def __init__(self, value, depth=None) :
        super().__init__()
        self.value   = value
        self.is_leaf = True
        self.depth   = depth

class Decision_Tree() :
    def __init__(self, max_depth=10, min_pop=1, seed=0,split_criterion="random", root=None) :
        self.rng               = np.random.default_rng(seed)
        if root :
            self.root          = root
        else :
            self.root          = Node(is_root=True)
        self.explanatory       = None
        self.target            = None
        self.max_depth         = max_depth
        self.min_pop           = min_pop
        self.split_criterion   = split_criterion
        self.predict           = None
```

- Once built, decision trees are binary trees : a node either is a leaf or has two children. It never happens that a node for which `is_leaf` is `False` has its `left_child` or `right_child` left unspecified.
- The first three tasks are a warm-up designed to review the basics of class inheritance and recursion (nevertheless, the functions coded in these tasks will be reused in the rest of the project).
- Our first objective will be to write a `Decision_Tree.predict` method that takes the explanatory features of a set of individuals and returns the predicted target value for these individuals.
- Then we will write a method `Decision_Tree.fit` that takes the explanatory features and the targets of a set of individuals, and grows the tree from the root to the leaves to make it in an efficient prediction tool.
- Once these tasks will be accomplished, we will introduce a new class `Random_Forest` that will also be a powerful prediction tool.
- Finally, we will write a variation on `Random_Forest`, called `Isolation_Random_forest`, that will be a tool to detect outliers.


## Task 0. Depth of a decision tree
All the nodes of a decision tree have their depth attribute. The depth of the root is 0 , while the children of a node at depth k have a depth of k+1. We want to find the maximum of the depths of the nodes (including the leaves) in a decision tree. In order to do so, we added a method def depth(self): in the Decision_Treeclass, a method def max_depth_below(self): in the Leaf class.

Task: Update the class Node by adding the method def max_depth_below(self):.


- File: [0-build_decision_tree.py](0-build_decision_tree.py)


## Task 1. Number of nodes/leaves in a decision tree

We now want to count the number of nodes in a decision tree, potentially excluding the root and internal nodes to count only the leaves. In order to do so, we added a method `def count_nodes(self, only_leaves=False):` in the `Decision_Tree` class:

```
def count_nodes(self, only_leaves=False) :
    return self.root.count_nodes_below(only_leaves=only_leaves)
```
we added a method `def count_nodes_below(self, only_leaves=False):` in the `Leaf` class:

```
def count_nodes_below(self, only_leaves=False) :
    return 1
```
Task: Update the class `Node` by adding the method `def count_nodes_below(self, only_leaves=False):`

- File: [1-build_decision_tree.py](1-build_decision_tree.py)

## Task 2. Let's print our Tree

In this task, we give you the `def __str__(self):` method for the `Decision_Tree` class :

```
def __str__(self):
    return self.root.__str__()
```
and the def __str__(self) : method for the Leaf class :
```
def __str__(self):
    return (f"-> leaf [value={self.value}]")
```

Task: Insert the above declarations in the respective classes, and update the class `Node` by adding the method `def __str__(self)` 

- File: [2-build_decision_tree.py](2-build_decision_tree.py)

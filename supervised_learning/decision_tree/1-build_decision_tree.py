#!/usr/bin/env python3
"""
This module defines classes for building and managing a decision tree.
"""
import numpy as np


class Node:
    """
    This class represents a node of a decision tree.
    """
    def __init__(self, feature=None, threshold=None,
                 left_child=None, right_child=None, is_root=False, depth=0):
        """
        Initialize a Node.
        Args:
            feature: Feature used to split the node.
            threshold: Threshold used to split the node.
            left_child: Left child of the node.
            right_child: Right child of the node.
            is_root: Whether the node is the root of the tree.
            depth: Depth of the node in the tree.
        """
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """
        Return the maximum depth of the nodes below this node.
        """
        return max(
            self.left_child.max_depth_below(),
            self.right_child.max_depth_below()
        )

    def count_nodes_below(self, only_leaves=False):
        """
        Count the nodes below this node.
        Args:
            only_leaves: If True, count only leaf nodes.
        Returns:
            The number of nodes in the subtree.
        """
        count = 0 if only_leaves else 1
        count += self.left_child.count_nodes_below(only_leaves)
        count += self.right_child.count_nodes_below(only_leaves)
        return count


class Leaf(Node):
    """
    This class represents a leaf of a decision tree.
    """
    def __init__(self, value, depth=None):
        """
        Initialize a Leaf.
        Args:
            value: Value associated with the leaf.
            depth: Depth of the leaf in the tree.
        """
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """
        Return the depth of the leaf.
        """
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """
        Count this leaf node.
        Args:
            only_leaves: Whether to count only leaf nodes.
        Returns:
            1, since a leaf is always one node.
        """
        return 1


class Decision_Tree():
    """
    This class represents a decision tree.
    """
    def __init__(self, max_depth=10, min_pop=1,
                 seed=0, split_criterion="random", root=None):
        """ Initialize a decision tree.
        Args:
            max_depth: Maximum allowed depth of the tree.
            min_pop: Minimum population required for a split.
            seed: Seed used to initialize the random generator.
            split_criterion: Criterion used to select tree splits.
            root: Root node of the tree. If None, a new root is created.
        """
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """
        Return the maximum depth of the decision tree.
        """
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """
        Count the nodes in the decision tree.
        Args:
            only_leaves: If True, count only the leaf nodes.
        Returns:
            The number of nodes in the tree.
        """
        return self.root.count_nodes_below(only_leaves=only_leaves)

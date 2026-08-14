#!/usr/bin/env python3
"""
This module defines a class for building and
managing isolation random trees
"""
import numpy as np
Node = __import__('8-build_decision_tree').Node
Leaf = __import__('8-build_decision_tree').Leaf


class Isolation_Random_Tree():
    """
    Represents a random isolation tree used for anomaly detection.
    """
    def __init__(self, max_depth=10, seed=0, root=None):
        """
        Initialize an isolation random tree.
        Args:
            max_depth: Maximum depth allowed for the tree.
            seed: Seed used to initialize the random generator.
            root: Root node of the tree. If None, a new root is created.
        """
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.max_depth = max_depth
        self.predict = None
        self.min_pop = 1

    def __str__(self):
        """
        Return the string representation of the decision tree.
        Returns:
            A string representation of the tree starting from its root.
        """
        return self.root.__str__()

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

    def update_bounds(self):
        """
        Compute the bounds for all nodes in the decision tree.
        The calculation starts from the root and recursively propagates
        the lower and upper bounds to all nodes.
        """
        self.root.update_bounds_below()

    def get_leaves(self):
        """
        Return a list containing all leaves of the tree.
        Returns:
            A list of all leaves in the decision tree.
        """
        return self.root.get_leaves_below()

    def pred(self, x):
        """
        Return the prediction of the decision tree.
        """
        return self.root.pred(x)

    def update_predict(self):
        """
        Update the prediction of the decision tree.
        """
        self.update_bounds()
        leaves = self.get_leaves()
        for leaf in leaves:
            leaf.update_indicator()
        self.predict = lambda A: np.array([self.pred(x) for x in A])

    def np_extrema(self, arr):
        """
        Return the minimum and maximum values of an array.
        Args:
            arr: Input NumPy array.
        Returns:
            A tuple containing the minimum and maximum values.
        """        
        return np.min(arr), np.max(arr)

    def random_split_criterion(self, node):
        """
        Randomly select a feature and threshold to split a node.
        Args:
            node: Node to split.
        Returns:
            A tuple containing the selected feature and threshold.
        """
        diff = 0
        while diff == 0:
            feature = self.rng.integers(0, self.explanatory.shape[1])
            feature_min, feature_max = self.np_extrema(
                self.explanatory[:, feature][node.sub_population]
                )
            diff = feature_max-feature_min
        x = self.rng.uniform()
        threshold = (1 - x) * feature_min + x * feature_max
        return feature, threshold

    def get_leaf_child(self, node, sub_population):
        """
        Create a leaf child with the most common target value.
        Args:
            node: Parent node.
            sub_population: Boolean mask of samples belonging to the leaf.
        Returns:
            The newly created leaf node.
        """
        leaf_child = Leaf(node.depth + 1)
        leaf_child.depth = node.depth + 1
        leaf_child.subpopulation = sub_population
        return leaf_child

    def get_node_child(self, node, sub_population):
        """
        Create an internal child node.
        Args:
            node: Parent node.
            sub_population: Boolean mask of samples belonging to the child.
        Returns:
            The newly created child node.
        """
        n = Node()
        n.depth = node.depth + 1
        n.sub_population = sub_population
        return n

    def fit_node(self, node):
        """
        Recursively split a node and create its children.
        Args:
            node: Node to split.
        """
        node.feature, node.threshold = self.random_split_criterion(node)

        left_population = node.sub_population & (
            self.explanatory[:, node.feature] > node.threshold
            )
        right_population = node.sub_population & (
            self.explanatory[:, node.feature] <= node.threshold
            )

        # Is left node a leaf ?
        is_left_leaf = (
            node.depth + 1 >= self.max_depth
            or left_population.sum() <= self.min_pop
        )

        if is_left_leaf:
            node.left_child = self.get_leaf_child(node, left_population)
        else:
            node.left_child = self.get_node_child(node, left_population)
            self.fit_node(node.left_child)

        # Is right node a leaf ?
        is_right_leaf = (
            node.depth + 1 >= self.max_depth
            or right_population.sum() <= self.min_pop
        )

        if is_right_leaf:
            node.right_child = self.get_leaf_child(node, right_population)
        else:
            node.right_child = self.get_node_child(node, right_population)
            self.fit_node(node.right_child)

    def fit(self, explanatory, verbose=0):
        """
        Train the decision tree using explanatory data and target values.
        Args:
            explanatory: Training input data.
            target: Target values associated with the input data.
            verbose: If 1, display training information.
        """
        self.split_criterion = self.random_split_criterion
        self.explanatory = explanatory
        self.root.sub_population = np.ones_like(
                explanatory.shape[0], dtype='bool'
            )

        self.fit_node(self.root)
        self.update_predict()

        if verbose == 1:
            print(f"""  Training finished.
    - Depth                     : {self.depth()}
    - Number of nodes           : {self.count_nodes()}
    - Number of leaves          : {self.count_nodes(only_leaves=True)}""")

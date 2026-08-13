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

    def left_child_add_prefix(self, text):
        """
        Add the prefix used to display the left child.
        Args:
            text: String representation of the child.
        Returns:
            The formatted string with the left-child prefix.
        """
        lines = text.split("\n")
        new_text = "    +--"+lines[0]+"\n"
        for x in lines[1:]:
            new_text += ("    |  "+x)+"\n"
        return (new_text)

    def right_child_add_prefix(self, text):
        """
        Add the prefix used to display the right child.
        Args:
            text: String representation of the child.
        Returns:
            The formatted string with the right-child prefix.
        """
        lines = text.split("\n")
        new_text = "    +--"+lines[0]+"\n"
        for x in lines[1:]:
            new_text += ("       "+x)+"\n"
        return (new_text)

    def __str__(self):
        """
        Return the string representation of the node.
        The representation includes the node's feature and threshold,
        followed by the formatted representations of its children.
        Returns:
            A string representation of the node and its subtree.
        """
        if self.is_root:
            text = (
                f"root [feature={self.feature}, "
                f"threshold={self.threshold}]\n"
            )
        else:
            text = (
                f"-> node [feature={self.feature}, "
                f"threshold={self.threshold}]\n"
            )
        left = self.left_child.__str__().rstrip("\n")
        right = self.right_child.__str__().rstrip("\n")

        text += self.left_child_add_prefix(left)
        text += self.right_child_add_prefix(right)
        return text

    def get_leaves_below(self):
        """
        Return a list containing all leaves below this node.
        Returns:
            A list of all leaves in the subtree.
        """
        return (
            self.left_child.get_leaves_below()
            + self.right_child.get_leaves_below()
        )

    def update_bounds_below(self):
        """
        Compute and update the bounds for this node's children.
        The bounds represent the minimum and maximum values allowed
        for each feature based on the splits in the tree.
        """
        if self.is_root:
            self.upper = {0: np.inf}
            self.lower = {0: -1*np.inf}

        for child in [self.left_child, self.right_child]:
            child.lower = self.lower.copy()
            child.upper = self.upper.copy()

        self.left_child.lower[self.feature] = self.threshold
        self.right_child.upper[self.feature] = self.threshold

        for child in [self.left_child, self.right_child]:
            child.update_bounds_below()

    def update_indicator(self):
        """
        Update the indicator based on the node's bounds.
        """
        def is_large_enough(x):
            """
            Check whether values are above the lower bounds.
            """
            return np.all(
                np.array([np.greater(x[:, key], self.lower[key])
                          for key in list(self.lower.keys())]), axis=0
                          )

        def is_small_enough(x):
            """
            Check whether values are below the upper bounds.
            """
            return np.all(
                np.array([np.less_equal(x[:, key], self.upper[key])
                          for key in list(self.upper.keys())]), axis=0
                          )

        self.indicator = lambda x: np.all(
            np.array([is_large_enough(x), is_small_enough(x)]), axis=0
            )

    def pred(self, x):
        """
        Recursively compute the prediction for the given input
        """
        if x[self.feature] > self.threshold:
            return self.left_child.pred(x)
        else:
            return self.right_child.pred(x)


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

    def __str__(self):
        """
        Return the string representation of the leaf.
        Returns:
            A string containing the value stored in the leaf.
        """
        return (f"-> leaf [value={self.value}]")

    def get_leaves_below(self):
        """
        Return this leaf as a list.
        Returns:
            A list containing this leaf.
        """
        return [self]

    def update_bounds_below(self):
        """
        Keep the bounds inherited from the parent node.
        A leaf has no children, so no further bounds need to be updated.
        """
        pass

    def pred(self, x):
        """
        Return the prediction of this leaf.
        """
        return self.value


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

    def __str__(self):
        """
        Return the string representation of the decision tree.
        Returns:
            A string representation of the tree starting from its root.
        """
        return self.root.__str__()

    def get_leaves(self):
        """
        Return a list containing all leaves of the tree.
        Returns:
            A list of all leaves in the decision tree.
        """
        return self.root.get_leaves_below()

    def update_bounds(self):
        """
        Compute the bounds for all nodes in the decision tree.
        The calculation starts from the root and recursively propagates
        the lower and upper bounds to all nodes.
        """
        self.root.update_bounds_below()

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

    def fit(self, explanatory, target, verbose=0):
        """
        Train the decision tree using explanatory data and target values.
        Args:
            explanatory: Training input data.
            target: Target values associated with the input data.
            verbose: If 1, display training information.
        """
        if self.split_criterion == "random":
            self.split_criterion = self.random_split_criterion
        else:
            self.split_criterion = self.Gini_split_criterion
        self.explanatory = explanatory
        self.target = target
        self.root.sub_population = np.ones_like(self.target, dtype='bool')

        self.fit_node(self.root)    # <--- to be defined later

        self.update_predict()    # <--- defined in the previous task

        if verbose == 1:
                print(f"""  Training finished.
- Depth                     : { self.depth()       }
- Number of nodes           : { self.count_nodes() }
- Number of leaves          : { self.count_nodes(only_leaves=True) }
- Accuracy on training data : { self.accuracy(self.explanatory, self.target)    }""")

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

    def fit_node(self, node):
        """
        Recursively split a node and create its children.
        Args:
            node: Node to split.
        """
        node.feature, node.threshold = self.split_criterion(node)

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
            or np.all(self.target[left_population] == self.target[left_population][0])
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
            or np.all(self.target[right_population] == self.target[right_population][0])
            )

        if is_right_leaf:
            node.right_child = self.get_leaf_child(node, right_population)
        else:
            node.right_child = self.get_node_child(node, right_population)
            self.fit_node(node.right_child)

    def get_leaf_child(self, node, sub_population):
        """
        Create a leaf child with the most common target value.
        Args:
            node: Parent node.
            sub_population: Boolean mask of samples belonging to the leaf.
        Returns:
            The newly created leaf node.
        """
        value = np.argmax(np.bincount(self.target[sub_population]))
        leaf_child = Leaf(value)
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

    def accuracy(self, test_explanatory, test_target):
        """
        Calculate the prediction accuracy of the decision tree.
        Args:
            test_explanatory: Input data used for evaluation.
            test_target: Expected target values.
        Returns:
            The proportion of correctly predicted values.
        """
        return np.sum(
            np.equal(self.predict(test_explanatory), test_target)
            ) / test_target.size

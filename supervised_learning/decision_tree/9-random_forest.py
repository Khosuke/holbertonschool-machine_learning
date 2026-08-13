#!/usr/bin/env python3
"""
This module defines a class for building and managing random forests.
"""
import numpy as np
Decision_Tree = __import__('8-build_decision_tree').Decision_Tree


class Random_Forest():
    """
    This class represents a Random Forest.
    """
    def __init__(self, n_trees=100, max_depth=10, min_pop=1, seed=0):
        """
        Initialize the Random Forest.
        Args:
            n_trees: Number of trees to grow in the forest.
            max_depth: Maximum depth allowed for each tree.
            min_pop: Minimum number of samples required to split a node.
            seed: Base random seed
        """
        self.numpy_predicts = []
        self.target = None
        self.numpy_preds = None
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.seed = seed

    def predict(self, explanatory):
        """
        Predict target values for the given examples using majority
        vote across all trees in the forest.
        Args:
            explanatory: Array containing the examples to classify.
        Returns:
            A NumPy array containing the predicted class for each example.
        """
        # Get predictions from each tree
        # Shape: (n_trees, n_samples)
        pred_list = np.array(
            [predict(explanatory)
             for predict in self.numpy_preds]
             )

        n_classes = int(pred_list.max()) + 1

        # counts[n, c] → number of trees that predicted class c for sample n
        # Shape: (n_samples, n_classes)
        counts = (pred_list[:, :, None] == np.arange(n_classes)).sum(axis=0)

        # Majority vote: class with the most votes for each sample
        return np.argmax(counts, axis=1)

    def fit(self, explanatory, target, n_trees=100, verbose=0):
        """
        Train the forest by fitting n_trees independent
        decision trees on the same data.
        Args:
            explanatory: Array containing the examples to classify.
            target: Array containing the class labels
              for each training example.
            n_trees: Number of trees to train.
            verbose: If 1, print training statistics after fitting.
        """
        self.target = target
        self.explanatory = explanatory
        self.numpy_preds = []
        depths = []
        nodes = []
        leaves = []
        accuracies = []
        for i in range(n_trees):
            T = Decision_Tree(
                max_depth=self.max_depth,
                min_pop=self.min_pop,
                seed=self.seed + i
                )
            T.fit(explanatory, target)
            self.numpy_preds.append(T.predict)
            depths.append(T.depth())
            nodes.append(T.count_nodes())
            leaves.append(T.count_nodes(only_leaves=True))
            accuracies.append(T.accuracy(T.explanatory, T.target))
        if verbose == 1:
            print(f"""  Training finished.
    - Mean depth                     : {np.array(depths).mean()}
    - Mean number of nodes           : {np.array(nodes).mean()}
    - Mean number of leaves          : {np.array(leaves).mean()}
    - Mean accuracy on training data : {np.array(accuracies).mean()}
    - Accuracy of the forest on td   : {
                self.accuracy(self.explanatory, self.target)
            }""")

    def accuracy(self, test_explanatory, test_target):
        """
        Compute the accuracy of the forest on a given test set.
        Args:
            test_explanatory: Array containing the test examples.
            test_target: Array containing the true class
                labels for the test examples.
        Returns:
            The proportion of correctly classified examples.
        """
        return np.sum(
            np.equal(self.predict(test_explanatory), test_target)
            ) / test_target.size

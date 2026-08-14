#!/usr/bin/env python3
"""
This module defines an Isolation Random Forest for anomaly detection.
"""
import numpy as np
Isolation_Random_Tree = __import__('10-isolation_tree').Isolation_Random_Tree


class Isolation_Random_Forest():
    """
    Represents a forest of random isolation trees.
    """
    def __init__(self, n_trees=100, max_depth=10, min_pop=1, seed=0):
        """
        Initialize an isolation random forest.
        Args:
            n_trees: Number of isolation trees in the forest.
            max_depth: Maximum depth allowed for each tree.
            min_pop: Minimum population required in a node.
            seed: Seed used to initialize the random trees.
        """
        self.numpy_predicts = []
        self.target = None
        self.numpy_preds = None
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.seed = seed

    def predict(self, explanatory):
        """
        Predict the mean isolation depth for each observation.
        Args:
            explanatory: Array containing the observations to evaluate.
        Returns:
            A NumPy array containing the mean prediction
            across all isolation trees.
        """
        predictions = np.array([f(explanatory) for f in self.numpy_preds])
        return predictions.mean(axis=0)

    def fit(self, explanatory, n_trees=100, verbose=0):
        """
        Train the isolation forest using multiple random trees.
        Args:
            explanatory: Array containing the training observations.
            n_trees: Number of trees to create.
            verbose: If 1, display training information.
        """
        if np.unique(explanatory, axis=0).shape[0] != explanatory.shape[0]:
            raise ValueError("Dataset contains duplicate observations")
        self.explanatory = explanatory
        self.numpy_preds = []
        depths = []
        nodes = []
        leaves = []
        for i in range(n_trees):
            T = Isolation_Random_Tree(
                    max_depth=self.max_depth, seed=self.seed+i
                )
            T.fit(explanatory)
            self.numpy_preds.append(T.predict)
            depths.append(T.depth())
            nodes.append(T.count_nodes())
            leaves.append(T.count_nodes(only_leaves=True))
        if verbose == 1:
            print(f"""  Training finished.
    - Mean depth                     : {np.array(depths).mean()}
    - Mean number of nodes           : {np.array(nodes).mean()}
    - Mean number of leaves          : {np.array(leaves).mean()}""")

    def suspects(self, explanatory, n_suspects):
        """
        returns the n_suspects rows in explanatory
        that have the smallest mean depth
        """
        depths = self.predict(explanatory)
        indices = np.argsort(depths)

        suspects = explanatory[indices[:n_suspects]]
        suspects_depths = depths[indices[:n_suspects]]

        return suspects, suspects_depths

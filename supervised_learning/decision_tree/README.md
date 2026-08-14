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

## Task 3. Towards the predict function (1) : the get_leaves method

Task: Insert the following declarations in their respective classes, and update the class `Node` by adding the method `def get_leaves_below(self):` that returns the list of all leaves of the tree.

Add in class `Leaf`:
```
def get_leaves_below(self) :
    return [self]
```
Add in class `Decision_Tree`:
```
def get_leaves(self) :
    return self.root.get_leaves_below()
```

- File [3-build_decision_tree.py](3-build_decision_tree.py)

## Task 4. Towards the predict function (2) : the update_bounds method

Task: Insert the following declarations in their respective classes, and update the class `Node` by completing the method `def update_bounds_below(self):`

This method should recursively compute, for each node, two dictionaries stored as attributes `Node.lower` and `Node.upper`.

These dictionaries should contain the bounds of the node for each feature.

The lower and upper bounds represent the minimum and maximum values, respectively, observed in the data subset associated with that node.

The keys in the dictionary represent the features.

Add in class `Leaf`:
```
    def update_bounds_below(self) :
        pass 
```
Add in class `Decision_Tree`:
```
    def update_bounds(self) :
        self.root.update_bounds_below()
```
Fill in `def update_bounds_below(self):` in class Node:
```
    def update_bounds_below(self) :
        if self.is_root : 
            self.upper = { 0:np.inf }
            self.lower = {0 : -1*np.inf }

        for child in [self.left_child, self.right_child] :

        # To Fill : compute and attach the lower and upper dictionaries to the children

        for child in [self.left_child, self.right_child] :
            child.update_bounds_below()
```

- File: [4-build_decision_tree.py](4-build_decision_tree.py)

## Task 5. Towards the predict function (3): the update_indicator method

Consider the indicator function for a given node, denoted as "n." This function is defined as follows:

It takes a 2D NumPy array, denoted as `A`, of shape `(n_individuals, n_features)`.
The output of the indicator function is a 1D NumPy array, of size equals to the number of individuals (`n_individuals`), containing boolean values.
The i-th element of this output array is set to `True` if the corresponding `i`-th individual meets the conditions specified by the node "n"; otherwise, it is set to `False`.
Task: Write a method `Node.update_indicator` that computes the indicator function from the `Node.lower` and `Node.upper` dictionaries and stores it in an attribute `Node.indicator` :

Fill in `def update_indicator(self):` in class `Node`:
```
def update_indicator(self) :

        def is_large_enough(x):

                #<- fill the gap : this function returns a 1D numpy array of size 
                #`n_individuals` so that the `i`-th element of the later is `True` 
                # if the `i`-th individual has all its features > the lower bounds

        def is_small_enough(x):

                #<- fill the gap : this function returns a 1D numpy array of size 
                #`n_individuals` so that the `i`-th element of the later is `True` 
                # if the `i`-th individual has all its features <= the lower bounds

        self.indicator = lambda x : np.all(np.array([is_large_enough(x),is_small_enough(x)]),axis=0)
```
- File: [5-build_decision_tree.py](5-build_decision_tree.py)

## Task 6. The predict function


We are now in a position to write our efficient Decision_Tree.predict function.

Task: Write a method `Decision_Tree.update_predict` that computes the prediction function :

Fill in `def update_predict(self):` in class `Decision_Tree`:
```
def update_predict(self):
        self.update_bounds()
        leaves = self.get_leaves()
        for leaf in leaves:
            leaf.update_indicator()          
        self.predict = lambda A: #<--- To be filled
```

As part of the testing process, insert the following methods into their respective classes:

add `def pred(self, x):` in class `Leaf`:
```
    def pred(self, x):
        return self.value
```
add `def pred(self,x):` in class `Node`:
```
    def pred(self, x):
        if x[self.feature]>self.threshold :
            return self.left_child.pred(x)
        else :
            return self.right_child.pred(x)
```
add `def pred(self, x):` in class `Decision_Tree`:
```
    def pred(self, x):
            return self.root.pred(x)
```

Now, to validate whether Decision_Tree.pred performs similarly to the existing Decision_Tree.predict, we are creating a generator for random trees. We will compare the behavior of Decision_Tree.predict and Decision_Tree.pred on a sample explanatory array.

- File: [6-build_decision_tree.py](6-build_decision_tree.py)


## Task 7. Training decision trees


Now we want to make our trees trainable, so we will write a method `Decision_Tree.fit` so that, when given

- a 2D numpy array `explanatory` of shape `(number of individuals, number of features)`.
- a 1D numpy array `target` of size `number of individuals`.
and evaluating the code below, should return a decision tree to make predictions.

```
T=Decision_Tree()
T.fit(explanatory,target)
```
The `fit` function
The code below showcases the fit function. As you can observe, we assign a value to the attribute `self.root.sub_population`. During the training, each node we build will have this attribute assigned with a 1D numpy array of booleans of size `target.size` (which is the number of individuals in the training set). The `i`-th value of this array is `True` if and only if the `i`-th individual visits the node (so for the root, all the values are `True` as you can see).

To be added in the `Decision_Tree` class :
```
def fit(self,explanatory, target,verbose=0) :
        if self.split_criterion == "random" : 
                self.split_criterion = self.random_split_criterion
        else : 
                self.split_criterion = self.Gini_split_criterion     <--- to be defined later
        self.explanatory = explanatory
        self.target      = target
        self.root.sub_population = np.ones_like(self.target,dtype='bool')

        self.fit_node(self.root)     <--- to be defined later

        self.update_predict()     <--- defined in the previous task

        if verbose==1 :
                print(f"""  Training finished.
- Depth                     : { self.depth()       }
- Number of nodes           : { self.count_nodes() }
- Number of leaves          : { self.count_nodes(only_leaves=True) }
- Accuracy on training data : { self.accuracy(self.explanatory,self.target)    }""")     <--- to be defined later
```

The `split` function
The training procedure consists in iteratively choosing splits from the root on, and the procedure to choose the splits depend on the situation, so, as you can see above, our training method will depend on an attribute `Decision_Tree.split_criterion`. For now, we will use a completely random way to split our nodes :

To be added in the `Decision_Tree` class :
```
    def np_extrema(self,arr):
        return np.min(arr), np.max(arr)

    def random_split_criterion(self,node) :
        diff=0
        while diff==0 :
            feature=self.rng.integers(0,self.explanatory.shape[1])
            feature_min,feature_max=self.np_extrema(self.explanatory[:,feature][node.sub_population])
            diff=feature_max-feature_min
        x=self.rng.uniform()
        threshold= (1-x)*feature_min + x*feature_max
        return feature,threshold
```
Note: As surprising as it may be, and as we will check, this randomized procedure already has an interesting predicting power.

Task
Finally, as you see, the fit method just initializes some attributes of the tree and then calls a new method `Decision_Tree`.fit_node on the root. Your task is to update the class `Decision_Tree` by adding and completing the method def fit_node(self,node) :

- A node is a leaf if either it contains less than `min_pop` individuals, or its depth equals `max_depth` or all the individuals of the training set that come to this node are in the same class (i.e. have the same `target` value)
- The value to be computed for a leaf is the most represented class among the individuals that finish their trip in this leaf.
- At a node, the splitting criterion furnishes a feature index and a threshold. If the value of the selected feature on an individual that crosses this node is greater (strictly) than the threshold, then the individual goes in the left child, otherwise it goes in the right child.
- No for loop on the individuals should appear in your code. Use numpy functions everywhere to get an efficient program.
```
def fit_node(self,node) :
        node.feature, node.threshold = self.split_criterion(node)

        left_population  =      <--- to be filled
        right_population =      <--- to be filled

        # Is left node a leaf ?
        is_left_leaf =    <--- to be filled

        if is_left_leaf :
                node.left_child = self.get_leaf_child(node,left_population)                                                         
        else :
                node.left_child = self.get_node_child(node,left_population)
                self.fit_node(node.left_child)

        # Is right node a leaf ?
        is_right_leaf =    <--- to be filled

        if is_right_leaf :
                node.right_child = self.get_leaf_child(node,right_population)
        else :
                node.right_child = self.get_node_child(node,right_population)
                self.fit_node(node.right_child)    

def get_leaf_child(self, node, sub_population) :        
        value =    <-- to be filled
        leaf_child= Leaf( value )
        leaf_child.depth=node.depth+1
        leaf_child.subpopulation=sub_population
        return leaf_child

def get_node_child(self, node, sub_population) :        
        n= Node()
        n.depth=node.depth+1
        n.sub_population=sub_population
        return n

def accuracy(self, test_explanatory , test_target) :
        return np.sum(np.equal(self.predict(test_explanatory), test_target))/test_target.size
```

- File: [7-build_decision_tree.py](7-build_decision_tree.py)


## Task 8. Using Gini impurity function as a splitting criterion


For a node $N$ containing a population $P$ that is partitioned in $k+1$ classes: $P = P_0, P_1, \cdots, P_k$, the Gini impurity of $N$ is defined as

$$
\text{Gini}(N) = 1 - \sum_{i=0}^{k} p_i^2
$$

that also can be written as:

$$\text{Gini}(N)=1 - \left(\frac {|(P_0)|} {|(P)|} \right)^2 - \cdots - \left(\frac {|(P_k)|} {|(P)|} \right)^2 $$


The idea behind this definition is that

- if the population of a node is equally partitioned into many classes, the Gini impurity will be large
- if the population of a node comes mainly from one class, the Gini impurity will be small

So

- if the Gini impurity of a leaf is large, we cannot be very confident in the prediction function of this node
- if the Gini impurity of a leaf is small, we can have more confidence in the prediction function of this node

Hence the idea to split a node is to choose the feature and the threshold for which the average of the Gini impurities of the corresponding children is the smallest.

$$\text{Gini}_{\text{split}}(N) = \frac{\text{card}(P_{\text{left}})}{\text{card}(P)} \, \text{Gini}(P_{\text{left}}) + \frac{\text{card}(P_{\text{right}})}{\text{card}(P)} \, \text{Gini}(P_{\text{right}})$$

Task: To find this value :

- Update the the Decision_Tree class by adding the new methods down below.
- Fill in the gap in the method def Gini_split_criterion_one_feature(self,node,feature) :.
- No for or while loop allowed !

- File: [8-build_decision_tree.py](8-build_decision_tree.py)

## Task 9. Random forests

In this task, we will create a new class Random_Forest.

When training an object of this class on a dataset, it will build a large list of decision trees with random splitting criterion. Then to predict the class of an individual, it will ask each of those trees its prediction, and will choose the prediction that is the most frequent.

**Pros:** this method has advantages over the use of the Gini criterion

- when the training dataset is large : it can save CPU usage,
- in terms of stability : the result of this method should be almost the same on the various training subsets of a cross-validation procedure while the Gini based decision trees can be very different for each of these training subsets.

**Cons:** The Gini-based decision tree furnishes a model that has a clear, elementary interpretation. This interpretation can be used, once the decision tree, to further understand (in a human sense) the dependence between the explanatory data and the target.

**Task:** write the methods for the class Random_Forest

- File: [9-random_forest.py](9-random_forest.py)

## Task 10. IRF 1 : isolation random trees

A useful application that shares similar concepts involves utilizing random forests for detecting outliers.

Here we don't have any target, just an array A of explanatory features describing a set of individuals. To identify the individuals that are the more likely to be outliers, we will train a random forest, but this time (since there isn't any class) we won't stop the splitting process when all the individuals in the node are in the same class. Instead we will rely on the max_depth attribute to stop the training. Once trained, the predict function of a random tree applied to an individual will return the depth of the leaf it falled into. Outliers are likely to finish their trip alone in a leaf that has a small depth, so, averaging these predictions on a forest, the individuals that minimize the mean depth will be our suspects.

**Task:** Implement the Isolation_Random_Tree class following the above directions.

- File: [10-isolation_tree.py](10-isolation_tree.py)

## Task 11. IRF 2 : isolation random forests

implement the class Isolation_Forest following the directions. :

Complete the method def suspects(self,explanatory,n_suspects):

Warning: Duplicates in dataset can cause the programs below to enter infinite loops. It is therefore important to check first that there are none.

- File: [11-isolation_forest.py](11-isolation_forest.py)

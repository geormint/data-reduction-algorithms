# Study of the effect of metric distance in data reduction techniques for the K nearest neighbors classifier

## Introduction

The k-Nearest Neighbors (k-NN) algorithm is a widely used and efficient lazy classification method. It is a user-friendly classifier that finds applications in various fields.

Unlike other classifiers, the k-NN algorithm does not generate classification models. Instead, it relies on the training data whenever a new object needs to be categorized. To classify an object x, the algorithm examines the available training data and identifies the k objects (neighbors) that are closest to x based on a distance metric. The object x is then assigned to the most common class among the classes of its k nearest neighbors. This class, also known as the parent class, is determined through a process called nearest neighbor voting.

## Distance Metrics

Distance metrics are used in both the supervised (categorization) and unsupervised learning (clustering) to measure similarity between data points. The distance metrics used for the purpose of this thesis are as follow:

#### Euclidean

The length of a line segment connecting two points in Euclidean space is referred to as the Euclidean distance.

$d(p,q) = d(q,p) = \sqrt{(q_{1}-p_{1})^{2} + (q_{2}-p_{2})^{2} + \ldots + (q_{n}-p_{n})^{2}} = \sqrt{\sum\limits_{i=1}^n (q_{i}-p_{i})^{2}}$

#### Manhattan

The total length of the projections of the line segment onto the coordinate axes is equivalent to the length of the line segment itself. In simpler terms, it is the sum of the absolute disparities between the measurement values in all dimensions of the two points.

$d(p,q) = d(q,p) = \rvert q_{1}-p_{1} \lvert + \rvert q_{2}-p_{2} \lvert + \ldots + \rvert q_{n}-p_{n} \lvert = \sum\limits_{i=1}^n \rvert q_{i}-p_{i} \lvert$

#### Minkowski

The Minkowski distance is a metric on a vector-shaped vector that can be thought of as a generalization of both the Euclidean distance and the Manhattan distance.

$d(p,q) = d(q,p) = (\rvert q_{1}-p_{1} \lvert ^{p})^{1/p}+ (\rvert q_{2}-p_{2} \lvert ^{p})^{1/p} + \ldots + (\rvert q_{n}-p_{n} \lvert ^{p})^{1/p} = \sum\limits_{i=1}^n (\lvert x - y \rvert ^p)^{1/p}$

#### Chebyshev

Chebyshev distance, maximal measure or L∞ measure is a measure defined on a vector space where the distance between two vectors is the largest of their differences in any coordinate dimension

$d(p,q) = d(q,p) = max(\rvert q_{1}-p_{1} \lvert + \rvert q_{2}-p_{2} \lvert  + \ldots + \rvert q_{n}-p_{n} \lvert) = \sum\limits_{i=1}^n max \lvert q - p \rvert$

## Algorithms

#### Edited Nearest Neighbor

The quality of the training data is enhanced through the utilization of processing algorithms, which eliminate outliers, noise, and mislabeled objects. Additionally, these algorithms work towards smoothing the decision boundaries between various classes. The ultimate goal of the processing technique is to generate a training set that exhibits no overlap between classes. 

The ENN rule, which is the standard editing algorithm, serves as the foundation for all other processing algorithms. It is a straightforward rule to comprehend. Initially, the training dataset (TS) is set to be the same as the processed set (ES). The method then searches the TS and identifies the k nearest neighbors for each element x in the TS. If the majority of these nearest neighbors determine that x is misclassified, it is eliminated from the ES. In simpler terms, if the majority of the k nearest neighbors have a different class than x, then x is considered either noise or a point near the decision boundary between classes, and it is removed from the ES.

```
Input: TS, k
Output: ES
1: ES ← TS
2: for each x ∈ TS do
3: 	NNs ← find the k nearest to x neighbors in TS − {x}
4: 	majorClass ← find the most common class of NNs
5: 	if xclass ̸ = majorClass then
6: 		ES ← ES − {x}
7: 	end if
8: end for
9: return ES
```

The Condensed Nearest Neighbor (CNN) rule is the most ancient and widely used algorithm for condensation. The CNN rule constructs its condensation set based on a simple idea. Elements that are located in the "inner" data area of a class, which means away from the bounds class decision, are not useful during the classification process. Therefore, they can be eliminated without any loss of accuracy. The CNN rule adopts this idea and attempts to place only those objects in the compaction set that are in the data regions near the decision boundaries between the different classes. These specific items are the only necessary objects for the classification process.

The CNN rule starts by moving an element of the original training dataset (TS) to the compression set (CS). Then, the 1-NN rule is applied by the CNN rule, and the objects of the TS are categorized by scanning the elements of the CS. If an object is miscategorized, it moves from TS to CS. The algorithm continues until there are no moves from the TS to the CS during a complete traversal of the TS. This ensures that the content of TS is correctly categorized by the content of CS. The remaining content of the TS is deleted.

```
Input: TS
Output: CS
1: CS ← 0
2: pick an item of TS and move it to CS
3: repeat
4: 	stop ← TRUE
5: 	for each x ∈ TS do
6: 		NN ← Nearest Neighbour of x neighbors in CS
7: 		if NNclass ̸ = xclass then
8: 			CS ← CS ∪ {x}
9: 			TS ← TS − {x}
10: 			stop ← FALSE
11: 		end if
12: 	end for
13: until stop == TRUE no move during a pass of TS
14: discard TS
15: return CS
```
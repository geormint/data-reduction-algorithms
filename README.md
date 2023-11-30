# Study of the effect of metric distance in data reduction techniques for the K nearest neighbors classifier

### Introduction

The k-Nearest Neighbors (k-NN) algorithm is a widely used and efficient lazy classification method. It is a user-friendly classifier that finds applications in various fields.

Unlike other classifiers, the k-NN algorithm does not generate classification models. Instead, it relies on the training data whenever a new object needs to be categorized. To classify an object x, the algorithm examines the available training data and identifies the k objects (neighbors) that are closest to x based on a distance metric. The object x is then assigned to the most common class among the classes of its k nearest neighbors. This class, also known as the parent class, is determined through a process called nearest neighbor voting.

### Distance Metrics

Distance metrics are used in both the supervised (categorization) and unsupervised learning (clustering) to measure similarity between data points. The distance metrics used for the purpose of this thesis are as follow:

##### Euclidean

The length of a line segment connecting two points in Euclidean space is referred to as the Euclidean distance.

$d(p,q) = d(q,p) = \sqrt{(q_{1}-p_{1})^{2} + (q_{2}-p_{2})^{2} + \ldots + (q_{n}-p_{n})^{2}} = \sqrt{\sum\limits_{i=1}^n (q_{i}-p_{i})^{2}}$

##### Manhattan

The total length of the projections of the line segment onto the coordinate axes is equivalent to the length of the line segment itself. In simpler terms, it is the sum of the absolute disparities between the measurement values in all dimensions of the two points.

$d(p,q) = d(q,p) = \rvert q_{1}-p_{1} \lvert + \rvert q_{2}-p_{2} \lvert + \ldots + \rvert q_{n}-p_{n} \lvert = \sum\limits_{i=1}^n \rvert q_{i}-p_{i} \lvert$

##### Minkowski

The Minkowski distance is a metric on a vector-shaped vector that can be thought of as a generalization of both the Euclidean distance and the Manhattan distance.

$d(p,q) = d(q,p) = (\rvert q_{1}-p_{1} \lvert ^{p})^{1/p}+ (\rvert q_{2}-p_{2} \lvert ^{p})^{1/p} + \ldots + (\rvert q_{n}-p_{n} \lvert ^{p})^{1/p} = \sum\limits_{i=1}^n (\lvert x - y \rvert ^p)^{1/p}$

##### Chebyshev

Chebyshev distance, maximal measure or L∞ measure is a measure defined on a vector space where the distance between two vectors is the largest of their differences in any coordinate dimension

$d(p,q) = d(q,p) = max(\rvert q_{1}-p_{1} \lvert + \rvert q_{2}-p_{2} \lvert  + \ldots + \rvert q_{n}-p_{n} \lvert) = \sum\limits_{i=1}^n max \lvert q - p \rvert$

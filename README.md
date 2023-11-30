# Study of the effect of metric distance in data reduction techniques for the K nearest neighbors classifier

### Introduction

The k-Nearest Neighbors (k-NN) algorithm is a widely used and efficient lazy classification method. It is a user-friendly classifier that finds applications in various fields.

Unlike other classifiers, the k-NN algorithm does not generate classification models. Instead, it relies on the training data whenever a new object needs to be categorized. To classify an object x, the algorithm examines the available training data and identifies the k objects (neighbors) that are closest to x based on a distance metric. The object x is then assigned to the most common class among the classes of its k nearest neighbors. This class, also known as the parent class, is determined through a process called nearest neighbor voting.

##Distance Metrics

The distance metrics used for the purpose of these thesis are as follow:

##### Euclidean

The length of a line segment connecting two points in Euclidean space is referred to as the Euclidean distance.

$[d(p,q) = d(q,p) = \sqrt{(q_{1}-p_{1})^{2} + (q_{2}-p_{2})^{2} + \ldots + (q_{n}-p_{n})^{2}} = \sqrt{\sum\limits_{i=1}^n (q_{i}-p_{i})^{2}}$
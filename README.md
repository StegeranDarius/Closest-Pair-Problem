# Closest Pair Problem

The Closest Pair Problem is a fundamental problem in computational geometry and computer science that involves finding the two closest points in a set of given points in a Euclidean space. The problem has a wide range of applications in various fields such as computer graphics, pattern recognition, image processing, and geographic information systems.

## Problem Statement

Given a set of `n` points in a `d`-dimensional space, find the pair of points with the minimum Euclidean distance between them.

## Time Complexity

The problem can be solved in O(n^2) time using a brute-force approach, but more efficient algorithms have been developed with a lower time complexity, such as the divide-and-conquer algorithm, which has a time complexity of O(n log n).

## Applications

In practice, the closest pair problem is used in a variety of applications such as:

- Image processing, where it can be used to detect edges in an image
- Geographic information systems, where it can be used to find the closest pair of cities or landmarks.

```jsx
def dis_between_closest_in_strip(points, points_counts, min_dis=float("inf")):
    for i in range(min(6, points_counts - 1), points_counts):
        for j in range(max(0, i - 6), i):
            current_dis = euclidean_distance_sqr(points[i], points[j])
            if current_dis < min_dis:
                min_dis = current_dis
    return min_dis
```

## Research

In research, the closest pair problem has been extensively studied and various algorithms have been proposed to solve the problem efficiently. Some of the well-known algorithms are:

- J. Bentley, "Multidimensional divide-and-conquer," Communications of the ACM, vol. 23, no. 4, pp. 214-229, 1980, which has a time complexity of O(n log n) and is widely used in practice.
- M. Karger, D. Levine, R. Lewin, "A randomized algorithm for closest-point problems," Proceedings of the Annual ACM Symposium on Computational Geometry, pp. 1-10, 1995, which has a time complexity of O(n log n) with high probability.

References:

- J. Bentley, "Multidimensional divide-and-conquer," Communications of the ACM, vol. 23, no. 4, pp. 214-229, 1980
- M. Karger, D. Levine, R. Lewin, "A randomized algorithm for closest-point problems," Proceedings of the Annual ACM Symposium on Computational Geometry, pp. 1-10, 1995

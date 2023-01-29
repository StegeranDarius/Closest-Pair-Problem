# Closest Pair Problem

## Stegeran Darius Cosmin

### The problem

The Closest Pair Problem is a fundamental problem in computational geometry and computer science that involves finding the two closest points in a set of given points in a Euclidean space. The problem has a wide range of applications in various fields such as computer graphics, pattern recognition, image processing, and geographic information systems.

### Problem Statement

Given a set of `n` points in a `d`-dimensional space, find the pair of points with the minimum Euclidean distance between them.

### The approach

At first, you may think that this is easy, just go trough all the points and find the minimum distance between them, this is called the naive approach.

The naive approach or the brute force method for the closest pair of points problem involves checking the distance between every pair of points and finding the closest among them. In this approach, we compare the distance between all pairs of points and keep track of the closest pair of points. The time complexity of this approach is O(n^2) where n is the number of points. This approach can be used for small datasets where n is not large but becomes inefficient for large datasets.

### My solution

My app solves the closest pair problem using divide and conquer algorithm and has a UI that allows users to input parameters and visualize the results. The visualization shows the randomly generated points and the closest pair found by the algorithm.

![Untitled](Closest%20Pair%20Problem%2062ba5d12bab84cf29a118a2e0c00ef7a/Untitled.png)

### The algorithm

My algorithm seeks to find the closest pair of points in a set of points in a 2D plane. It uses a divide-and-conquer algorithm to find the closest pair of points.

For example, let's consider the set of points [(1, 2), (3, 4), (5, 6), (7, 8)].

Step 1: Sorting

- The code first sorts the points based on their x-coordinate and y-coordinate. So, the sorted points based on x-coordinate are [(1, 2), (3, 4), (5, 6), (7, 8)] and based on y-coordinate are [(1, 2), (3, 4), (5, 6), (7, 8)].

Step 2: Finding the closest pair of points - Base case

- If the number of points is less than or equal to 3, the code finds the closest pair of points using a nested loop and the euclidean distance formula. In this case, since the number of points is 4, it goes to step 3.

Step 3: Finding the closest pair of points - Divide-and-Conquer

- The code splits the set of points into two halves - left and right, and finds the closest pair of points in both halves using recursion.
- For the left half, it calls the function with the points [(1, 2), (3, 4)], the sorted points based on y-coordinate [(1, 2), (3, 4)], and the count 2.
- For the right half, it calls the function with the points [(5, 6), (7, 8)], the sorted points based on y-coordinate [(5, 6), (7, 8)], and the count 2.
- The closest pair of points in the left and right halves is [(1, 2), (3, 4)] with a distance of 2.82843.
- The code then finds the closest pair of points in a strip of width 2 * closest_pair_distance_left_and_right, which is 5.65686, on either side of the midpoint. In this case, the strip contains all 4 points.
- The closest pair of points in the strip is [(1, 2), (3, 4)] with a distance of 2.82843.
- Finally, the code returns the minimum of the closest pair of points in the left and right halves and the strip. In this case, it returns 2.82843.

Step 4: Final result

- The closest pair of points is [(1, 2), (3, 4)] with a distance of 2.82843.

![Untitled](Closest%20Pair%20Problem%2062ba5d12bab84cf29a118a2e0c00ef7a/Untitled%201.png)

```jsx
column_based_sort
    Input: an array of points and an integer representing the column (0 for x-coordinate, 1 for y-coordinate) to sort by
    Output: the sorted array of points based on the specified column
    Pseudocode:
    Sort the array of points based on the specified column using the "sorted" function with
			 a key function that returns the value at the specified column for each point
    Return the sorted array
```

```jsx
closest_pair_of_points_sqr
    Input: two arrays representing the points sorted on x-coordinate and y-coordinate respectively,
					 and an integer representing the number of points in the arrays
    Output: the minimum squared Euclidean distance between all pairs of points
    Pseudocode:

    If the number of points is less than or equal to 3:
        Return the minimum squared Euclidean distance between all pairs of points using the dis_between_closest_pair function
    Otherwise:
        Divide the points into two halves, left and right, by finding the middle point using integer division by 2
        Recursively find the minimum squared Euclidean distance in the left half using the closest_pair_of_points_sqr
					 function and the points sorted on x-coordinate and y-coordinate
        Recursively find the minimum squared Euclidean distance in the right half using the closest_pair_of_points_sqr
```

```jsx
euclidean_distance_sqr
    Input: two points represented as arrays [x1, y1] and [x2, y2]
    Output: the squared Euclidean distance between the two points
    Pseudocode:

    Calculate the difference between x-coordinates of the two points and square it
    Calculate the difference between y-coordinates of the two points and square it
    Return the sum of the above two differences
```

```jsx
dis_between_closest_in_strip
    Input: an array of points within a certain strip (as determined by the main function) 
				   and an integer representing the number of points in the strip
    Output: the minimum squared Euclidean distance between all pairs of points in the strip
    Pseudocode:

    Initialize a variable "min_dis" to infinity
    For each point in the strip (from 6 to n-1, or from 0 to n-1 if n is less than 6):
        For each point before the current point in the strip (from 0 to i-6 or 0 to i-1 if i is less than 6):
            Calculate the squared Euclidean distance between the two points using the euclidean_distance_sqr function
            If the current distance is less than the current minimum, update the minimum distance
    Return the minimum distance
```

## Time Complexity

The problem can be solved in O(n^2) time using a brute-force approach, but more efficient algorithms have been developed with a lower time complexity, such as the divide-and-conquer algorithm, which has a time complexity of O(n log n).

## Applications

In practice, the closest pair problem is used in a variety of applications such as:

- Image processing, where it can be used to detect edges in an image
- Geographic information systems, where it can be used to find the closest pair of cities or landmarks.

## Research

In research, the closest pair problem has been extensively studied and various algorithms have been proposed to solve the problem efficiently. Some of the well-known algorithms are:

- J. Bentley, "Multidimensional divide-and-conquer," Communications of the ACM, vol. 23, no. 4, pp. 214-229, 1980, which has a time complexity of O(n log n) and is widely used in practice.
- M. Karger, D. Levine, R. Lewin, "A randomized algorithm for closest-point problems," Proceedings of the Annual ACM Symposium on Computational Geometry, pp. 1-10, 1995, which has a time complexity of O(n log n) with high probability.

References:

- J. Bentley, "Multidimensional divide-and-conquer," Communications of the ACM, vol. 23, no. 4, pp. 214-229, 1980
- M. Karger, D. Levine, R. Lewin, "A randomized algorithm for closest-point problems," Proceedings of the Annual ACM Symposium on Computational Geometry, pp. 1-10, 1995
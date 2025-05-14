# Day 32: K-th Element of Two Sorted Arrays

## Problem Statement
Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.

## Constraints:
- Arrays are sorted.

- Both arrays can be large.

- You are not allowed to merge both arrays due to space and time constraints.

- Optimize for time using a binary search approach.

## Approach
We will use a Binary Search Partition Method (Optimized approach using divide and conquer):

1. Always apply binary search on the smaller array for efficiency.

2. Perform a partition on both arrays such that the total number of elements on the left side is k.

3. Ensure the left parts of both arrays are smaller than the right parts.

4. The answer will be the maximum element from the left sides.

## Algorithm Steps:
- Use Binary Search on the smaller array.

- Maintain low and high pointers based on the valid partition range.

- Calculate partition points (cutA, cutB).

- Check if the left side elements are smaller or equal to the right side.

- If yes, return the maximum of the left sides.

- Else, adjust the search boundaries accordingly.

- Handle edge cases using float('-inf') and float('inf').

## Complexity
- Time Complexity: O(log(min(n, m)))

- Space Complexity: O(1)

## Learning
1. Learned how to adapt binary search beyond single arrays.

2. Important lesson on partition logic and handling large inputs efficiently.

3. Powerful technique, often used in interview questions.

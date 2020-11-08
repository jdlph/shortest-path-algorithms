# Boost Shortest-Path Algorithm Implementations using Proper Data Structures

This sub-project will concentrate on the modified label correcting (MLC) algorithm and its three special implementations, and demonstrate how to boost their
performances in terms of running time by reducing some key operations from linear time to logarithm or constant time through introducing the following data structures.

1. Use an indicator array rather than the built-in x in s operation to check the presence
of an element x in a list/container s for all implementations,
2. Adopt the built-in deque to replace list and its pop(0) and insert(0, x) operations in
the deque implementation,
3. Replace the built-in deque with a simplified array-based deque for the deque
implementation,
4. Introduce binary heap (heapq) in the Minimum Distance Label implementation.

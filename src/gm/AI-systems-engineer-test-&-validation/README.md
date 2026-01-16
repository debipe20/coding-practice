# Common Algorithms – Interview Problems and Use Cases

---

## 1. Linear Search

### Interview Problem

**Problem:**
Given an array of integers `nums` and a target value `target`, search for the target in the array.
Return the index if found; otherwise, return `-1`.

### When and Why to Use

* Use when the data is **unsorted**
* Best for **small datasets**
* Simple and reliable, with no preconditions
* Often preferred in **safety-critical or validation systems** due to predictability

---

## 2. Binary Search

### Interview Problem

**Problem:**
Given a sorted array of integers `nums` in ascending order and a target value `target`, find the index of the target.
If the target does not exist, return `-1`.

### When and Why to Use

* Use when the data is **sorted**
* Much faster than linear search for large datasets
* Reduces search space by half each step
* Requires careful handling of boundaries and assumptions

---

## 3. Bubble Sort

### Interview Problem

**Problem:**
Given an array of integers `nums`, sort the array in ascending order using the Bubble Sort algorithm.

### When and Why to Use

* Rarely used in production
* Easy to understand and implement
* Useful for **learning**, **testing**, and **interview explanations**
* Good for discussing inefficiency and optimization

---

## 4. Merge Sort

### Interview Problem

**Problem:**
Given an array of integers `nums`, sort the array in ascending order using Merge Sort.

### When and Why to Use

* Use when **guaranteed performance** is required
* Time complexity is always O(n log n)
* Stable sort
* Suitable for **large datasets** and **external sorting**

---

## 5. Selection Sort

### Interview Problem

**Problem:**
Given an array of integers `nums`, sort the array in ascending order using Selection Sort.

### When and Why to Use

* Simple and deterministic
* Performs minimal swaps
* Useful when **write operations are expensive**
* Mainly used for learning and comparison

---

## 6. Quick Sort

### Interview Problem

**Problem:**
Given an array of integers `nums`, sort the array using the Quick Sort algorithm.

### When and Why to Use

* Very fast in practice
* Average time complexity is O(n log n)
* In-place sorting (low memory usage)
* Requires careful pivot selection to avoid worst-case behavior

---

## 7. Depth-First Search (DFS)

### Interview Problem

**Problem:**
Given a graph or tree, determine whether a path exists between two nodes using Depth-First Search.

### When and Why to Use

* Use for **deep traversal**
* Useful for path exploration, cycle detection
* Lower memory usage than BFS
* Common in tree-based problems

---

## 8. Breadth-First Search (BFS)

### Interview Problem

**Problem:**
Given a graph or tree, find the shortest path between two nodes using Breadth-First Search.

### When and Why to Use

* Use when the **shortest path** is required
* Explores level by level
* Guarantees minimum steps in unweighted graphs
* Requires more memory than DFS

---

## 9. Hash Lookup

### Interview Problem

**Problem:**
Given an array of integers `nums` and a target value `target`, determine if two numbers add up to the target using a hash map.

### When and Why to Use

* Fast lookup with average O(1) time
* Ideal for membership checks and key-based access
* Trades memory for speed
* Widely used in real-world systems

---

## Interview Summary Tip

Interviewers want to know:

* Can you **identify the right algorithm**?
* Can you **state preconditions**?
* Can you **explain trade-offs**?
* Can you reason about **performance and safety**?

---

*This document can be used directly in a GitHub repository or as interview preparation notes.*

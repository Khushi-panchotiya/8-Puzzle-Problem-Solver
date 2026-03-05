# 8-Puzzle State-Space Search Solver 🧩



This repository contains a robust, modular implementation of four fundamental search algorithms used to solve the classic 8-Puzzle problem. The project explores the intersection of uninformed and informed search strategies, demonstrating how different data structures and heuristic evaluations impact time complexity, space complexity, and optimal pathfinding.

## 📌 The Problem Domain
The 8-puzzle is a sliding puzzle consisting of a 3x3 grid with 8 numbered tiles and one blank space. The objective is to transition from a randomized initial state to a specified goal state by sliding tiles horizontally or vertically into the blank space. 

The state space consists of 9! / 2 = 181,440 reachable states.

## 🚀 Algorithms Implemented

This project implements and compares the following search strategies:

### 1. Breadth-First Search (BFS)
* **Approach:** Uninformed search exploring the state space level by level using a FIFO Queue.
* **Properties:** Complete and Optimal (guarantees the shortest path in terms of the number of moves).
* **Complexity:** Time and Space complexity are exponential, bounded by $O(b^d)$, where $b$ is the branching factor and $d$ is the depth of the optimal solution. 

### 2. Depth-First Search (DFS)
* **Approach:** Uninformed search exploring as far as possible along each branch before backtracking, utilizing a LIFO Stack.
* **Properties:** Not guaranteed to find the optimal path. Can be highly inefficient if it explores deep, non-optimal branches.
* **Complexity:** Highly space-efficient with a space complexity of $O(bm)$, where $m$ is the maximum depth. Time complexity remains exponential.

### 3. Best-First Search (Greedy)
* **Approach:** Informed search that expands the node closest to the goal state according to a heuristic function, $h(n)$. Implemented using a Priority Queue.
* **Properties:** Faster than uninformed searches but is neither complete nor optimal. It can get stuck in local loops depending on the heuristic.
* **Evaluation Function:** $f(n) = h(n)$

### 4. A* Search (A-Star)
* **Approach:** Advanced informed search that calculates the cost of the path taken so far, $g(n)$, and the estimated cost to the goal, $h(n)$. 
* **Properties:** Both Complete and Optimal (provided the heuristic is admissible). This algorithm strikes the best balance between performance and accuracy.
* **Evaluation Function:** $f(n) = g(n) + h(n)$

## 📐 Heuristics Used
The informed algorithms (Best-First and A*) utilize the following admissible heuristics to estimate $h(n)$:

1.  **Misplaced Tiles:** Counts the total number of tiles that are not in their goal position.
2.  **Manhattan Distance:** Calculates the sum of the absolute distances of each out-of-place tile from its goal position:
    $$h(n) = \sum (|x_{current} - x_{goal}| + |y_{current} - y_{goal}|)$$

## ⚖️ Algorithm Comparison

Here is a breakdown of the core theoretical metrics for each implemented algorithm:

**Key Variables:**
* **$b$**: Branching factor (maximum number of successors of any node; for 8-puzzle, $b \le 4$).
* **$d$**: Depth of the shallowest goal node (the optimal solution length).
* **$m$**: Maximum length of any path in the state space.

| Feature | Breadth-First (BFS) | Depth-First (DFS) | Best-First (Greedy) | A* Search |
| :--- | :--- | :--- | :--- | :--- |
| **Category** | Uninformed | Uninformed | Informed | Informed |
| **Evaluation Function** | None | None | $f(n) = h(n)$ | $f(n) = g(n) + h(n)$ |
| **Data Structure** | FIFO Queue | LIFO Stack | Priority Queue | Priority Queue |
| **Time Complexity** | $O(b^d)$ | $O(b^m)$ | $O(b^m)$ (worst case) | $O(b^d)$ (with good heuristic) |
| **Space Complexity** | $O(b^d)$ | $O(bm)$ | $O(b^m)$ (worst case) | $O(b^d)$ |
| **Complete?** | Yes | No | No | Yes |
| **Optimal?** | Yes | No | No | Yes (if $h(n)$ is admissible) |

### Performance on the 8-Puzzle

* **Breadth-First Search (BFS):** Guarantees the absolute shortest path to the solution. However, it is highly memory-intensive because it stores every node at the current depth level before moving deeper, causing the queue to grow exponentially.
* **Depth-First Search (DFS):** Highly space-efficient compared to BFS. However, it dives deep down a single path, meaning it takes incredibly long, non-optimal routes and can easily get trapped in infinite loops without strict cycle detection.
* **Best-First Search (Greedy):** Incredibly fast. By looking strictly at the heuristic $h(n)$, it aggressively pursues the goal and explores far fewer nodes. However, it acts with tunnel vision, ignoring the path cost $g(n)$, which often leads to a fast but sub-optimal solution.
* **A\* Search (The Gold Standard):** Both optimal and complete. By factoring in both the cost incurred so far $g(n)$ and the estimated distance to the goal $h(n)$, it avoids the tunnel vision of Best-First Search while severely restricting the massive memory footprint of BFS.

## 2024-05-24 - Python list buffer generation optimization
**Learning:** In Python, creating large byte arrays/lists by appending/extending inside a `for` loop (e.g. `for _ in range(W*H): buffer.extend([high, low])`) is an O(N) operation with significant overhead due to interpreter loop mechanics and method call overhead.
**Action:** Use list multiplication `[high, low] * (W * H)` instead. It leverages C-level array copying which is orders of magnitude faster (0.8s vs 0.013s for 100 iterations on a 240x240 screen).

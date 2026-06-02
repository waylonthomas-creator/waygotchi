
## 2026-06-02 - [Optimize _888_to_565 pure python fallback]
**Learning:** Pure Python framebuffer fallbacks require manual memory pre-allocation without numpy. Using byte string concatenation (`b += ...`) inside loops results in O(N^2) memory reallocation overhead.
**Action:** Always pre-allocate memory using `bytearray` and use direct bitwise logic and index assignments (e.g., `b[j] = val & 0xFF`) for high-performance byte packing in Python.

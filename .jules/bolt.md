## 2024-05-06 - Bytearray Pre-allocation for Framebuffer
**Learning:** Python's byte string concatenation (`b += ...`) inside loops creates O(N^2) memory reallocation overhead, which causes significant performance drops in UI drawing operations (like `_888_to_565` pure Python fallback for framebuffer).
**Action:** Always pre-allocate memory using `bytearray(size)` and use direct index assignment for fast buffer construction.

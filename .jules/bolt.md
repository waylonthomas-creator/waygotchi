## 2024-05-24 - Python byte string concatenation bottleneck
**Learning:** In pure Python fallback routines (like framebuffer pixel conversion `_888_to_565`), repeated byte string concatenation (`b += int.to_bytes(...)`) within a tight loop creates massive O(N^2) memory reallocation overhead. This causes extreme CPU bottlenecks for large buffers (like images).
**Action:** Always pre-allocate memory using `bytearray` and assign values directly via indexing and bitwise operations instead of `.to_bytes()` or `+=` concatenation.

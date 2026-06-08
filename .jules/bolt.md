## 2026-06-08 - Framebuffer Optimization
**Learning:** Python byte string concatenation (`b += ...`) inside loops creates severe O(N^2) memory reallocation overhead. Also, numpy isn't always available in embedded environments for `numpy_888_565`.
**Action:** Always pre-allocate memory using `bytearray` and use direct index assignment with bitwise operations (`val & 0xFF`, `val >> 8`). This improved `_888_to_565` execution time by over 15x.

## 2024-05-24 - Python byte concatenation overhead
**Learning:** In pure Python paths for UI framebuffer drawing (like `_888_to_565` missing numpy), using `b += ...` for byte concatenation inside loops causes O(N^2) memory reallocation overhead.
**Action:** Pre-allocate memory using `bytearray` and use direct index assignment with bitwise logic to avoid `int.to_bytes` overhead.

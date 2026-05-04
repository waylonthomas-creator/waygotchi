## 2024-05-04 - O(N^2) memory reallocation overhead in Python UI rendering
**Learning:** Pure-Python fallback functions for UI rendering, such as framebuffer pixel format conversion (`_888_to_565`), commonly suffer from O(N^2) memory reallocation overhead when accumulating byte strings with `+=` inside a loop.
**Action:** Always pre-allocate memory using `bytearray` of the exact required size and use direct index assignment (`b[i*2] = ...`) rather than byte string concatenation for massive speedups in hot loops without needing C-extensions or NumPy.

## 2026-06-06 - [Framebuffer Python 888 to 565 Conversion Optimization]
**Learning:** Using `b += int.to_bytes(...)` inside a loop for framebuffer processing causes massive O(N^2) memory reallocation overhead in pure Python.
**Action:** Always pre-allocate memory using `bytearray` and use direct index assignment with bitwise operations (`v & 0xFF`, `v >> 8`) instead of byte string concatenation and `int.to_bytes` when processing large buffers without numpy.

## 2026-05-29 - Optimize _888_to_565 framebuffer color conversion
**Learning:** For high-performance byte packing in Python, especially inside loops, applying direct bitwise logic and assigning the values directly into a pre-allocated bytearray is significantly faster than using int.to_bytes and string concatenation.
**Action:** Always pre-allocate memory using bytearray and use direct index assignment when constructing large byte buffers in Python.

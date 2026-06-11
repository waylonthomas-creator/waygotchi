## 2026-06-11 - Optimize 24-bit to 16-bit framebuffer color conversion
**Learning:** To avoid O(N^2) memory reallocation overhead when constructing large byte buffers in Python, always pre-allocate memory using `bytearray` and use direct index assignment with bitwise logic instead of relying on byte string concatenation (`b += ...`) and `int.to_bytes` inside a loop.
**Action:** Pre-allocate byte buffers and populate them with direct index assignments when performing hot-path conversions.

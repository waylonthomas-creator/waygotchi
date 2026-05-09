## 2024-05-24 - Framebuffer RGB to 565 Conversion Optimization
**Learning:** Python's byte string concatenation `b += ...` and `int.to_bytes` inside a high-frequency loop (like rendering an 800x480 RGB framebuffer) create significant overhead, turning O(N) tasks into O(N^2) due to reallocation.
**Action:** Use pre-allocated `bytearray` and direct bitwise assignment (e.g., `b[idx] = val & 0xFF`, `b[idx+1] = val >> 8`) for memory-bound, tight loops like framebuffer operations to achieve 30x+ performance gains.

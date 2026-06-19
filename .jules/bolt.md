## 2024-05-15 - Fast byte packing for framebuffers
**Learning:** Using `b += int.to_bytes(...)` inside a loop for constructing large byte buffers (like framebuffer pixels) causes O(N^2) memory reallocation overhead and is significantly slower than direct bitwise assignment.
**Action:** Always pre-allocate memory using `bytearray` and use direct index assignment with bitwise logic (e.g., `res[i] = val & 0xFF; res[i+1] = val >> 8`) instead of relying on byte string concatenation and `int.to_bytes`.

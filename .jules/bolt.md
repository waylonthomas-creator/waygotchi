## 2026-05-22 - Python Bytearray Optimization for Framebuffers
**Learning:** In pure Python environments on embedded hardware, converting image buffers using `b += int.to_bytes(...)` causes O(N^2) memory reallocation overhead.
**Action:** Always pre-allocate memory using `bytearray` and use direct index assignment with bitwise operations (`out[j] = val & 0xFF`) when processing large buffers.

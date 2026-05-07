## 2026-05-07 - Pre-allocating bytearray for framebuffer conversion optimization
**Learning:** Converting RGB888 to RGB565 via `b += int.to_bytes(...)` causes O(N^2) memory reallocation overhead when building large byte buffers in Python, significantly degrading performance.
**Action:** When working with large framebuffers or similar data arrays, avoid byte string concatenation (`b +=`) in a loop. Instead, pre-allocate memory using `bytearray` and use direct index assignment with bitwise shifting. This optimized the fallback `_888_to_565` loop in `fb.py` from ~7.5s to ~0.3s.

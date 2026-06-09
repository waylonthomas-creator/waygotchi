## 2026-06-09 - Framebuffer byte array allocation overhead
**Learning:** Using repeated byte string concatenation (`b += ...`) and `int.to_bytes` in pure Python framebuffer loops causes massive O(N^2) memory reallocation overhead (~30s for an 800x480 screen).
**Action:** Always pre-allocate memory using `bytearray` and apply direct bitwise logic and index assignments inside tight loops.

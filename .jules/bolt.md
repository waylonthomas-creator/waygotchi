## 2026-06-15 - [Python Bytearray vs String Concatenation in Framebuffer Fallback]
**Learning:** Pure Python framebuffer conversion (`_888_to_565`) has O(N^2) memory reallocation overhead when using `b += int.to_bytes(...)` inside a loop, causing UI lag on embedded hardware where numpy is missing.
**Action:** Always use a pre-allocated `bytearray` and direct bitwise assignment (`b[idx] = val & 0xFF`, `b[idx+1] = val >> 8`) instead of string concatenation inside large loops to achieve ~3x speedup.

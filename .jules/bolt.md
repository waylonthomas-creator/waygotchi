## 2024-04-29 - O(N^2) memory reallocation overhead when dealing with large byte buffers
**Learning:** Building large byte arrays piece-by-piece using `b += ...` inside a loop leads to serious O(N^2) memory reallocation overhead, especially noticeable when dealing with UI or framebuffer data sizes.
**Action:** Always pre-allocate memory using `bytearray` when constructing large byte buffers, and perform direct index assignments (`b[idx] = ...`) rather than string concatenations.

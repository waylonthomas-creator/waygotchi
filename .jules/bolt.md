## 2026-06-17 - [Performance] Pre-allocating byte buffers inside loops
**Learning:** To avoid O(N^2) memory reallocation overhead when constructing large byte buffers in Python, it's significantly faster to pre-allocate memory using `bytearray` and assign directly via index/bitmask than relying on string concatenation (`b += ...`) and `int.to_bytes()` inside a loop.
**Action:** Always pre-allocate memory using `bytearray` for large binary transformations inside loops and assign bytes via bitwise shift operations.

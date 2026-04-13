## 2024-05-19 - Removed O(N^2) byte concatenation overhead
**Learning:** Found a major performance bottleneck where bytes string concatenation `b += ...` inside a long loop converting RGB to RGB565 was creating an O(N^2) memory reallocation problem.
**Action:** Always pre-allocate memory (using `bytearray` or pre-sized lists) when constructing large buffers in Python, instead of relying on string or byte concatenation in a loop.

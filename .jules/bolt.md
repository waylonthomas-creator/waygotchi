## 2024-06-25 - Python Byte String Concatenation Bottleneck
**Learning:** In standard Python, repeatedly concatenating byte strings (`b += ...`) inside a loop results in an O(N^2) memory reallocation overhead. This is especially problematic for large pixel array manipulations (like framebuffer processing where numpy isn't available).
**Action:** Always pre-allocate memory using `bytearray` and use direct index assignment (or slice assignment) for such operations, which can be 5x+ faster than dynamic byte string concatenation.

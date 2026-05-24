## 2024-05-24 - Pre-allocate bytearrays for Python buffer construction
**Learning:** In Python, appending to byte strings (`b += ...`) inside a loop causes O(N^2) memory reallocation overhead. Additionally, `int.to_bytes` is slower than direct bitwise arithmetic.
**Action:** Always pre-allocate memory using `bytearray` and assign via index with bitwise operations (e.g., `val & 0xFF`) when constructing large buffers, such as in pure Python framebuffer conversions.

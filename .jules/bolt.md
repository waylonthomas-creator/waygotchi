
## 2024-05-24 - High-performance Byte Processing in Python
**Learning:** When performing bulk byte manipulations (like color format conversions from RGB888 to RGB565) in Python on embedded hardware, using standard byte string concatenation (`b += ...`) inside a loop causes O(N^2) memory reallocation overhead. Furthermore, `int.to_bytes` is relatively slow inside tight loops.
**Action:** Always pre-allocate memory using `bytearray` when size is known, and assign values directly by index. For byte packing, apply bitwise logic (e.g., `val & 0xFF`, `val >> 8`) and direct assignment (`out[idx] = ...`) rather than `int.to_bytes` to maximize loop efficiency.

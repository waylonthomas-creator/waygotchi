## 2024-05-18 - Avoid byte string concatenation in loops
**Learning:** Concatenating byte strings (`b += ...`) inside a loop for large image buffers (like in `_888_to_565`) causes O(N^2) memory reallocation overhead, taking almost 50 seconds for an 800x600 image. Also, `int.to_bytes` is relatively slow inside tight loops.
**Action:** Always pre-allocate memory using `bytearray` and use direct index assignment with bitwise operations (e.g., `b[idx] = val & 0xFF`, `b[idx + 1] = val >> 8`) for high-performance byte packing. This provides a ~137x speedup.

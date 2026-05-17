## 2024-05-17 - Avoid byte string concatenation in loops
**Learning:** In pure Python framebuffer handling (`_888_to_565`), iterating and appending to a bytes object using `b += int.to_bytes(...)` causes massive performance hits (~13.6s vs 0.3s for 800x600 displays) due to O(N^2) memory reallocation overhead.
**Action:** Always pre-allocate memory using `bytearray` and assign directly via index using bitwise logic (e.g. `b[j] = val & 0xFF; b[j+1] = val >> 8`) instead of `int.to_bytes` when dealing with large repeated buffer transformations.

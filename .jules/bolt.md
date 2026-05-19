## 2024-05-24 - [Avoid Python Byte String Concatenation in Loops]
**Learning:** Concatenating byte strings in Python (`b += ...`) inside a loop causes O(N^2) memory reallocation overhead, significantly slowing down data processing loops like those in `fb.py`'s fallback `_888_to_565` conversion.
**Action:** Use a pre-allocated `bytearray` and direct index assignment with bitwise logic (`val & 0xFF`) instead of `int.to_bytes`. This avoids reallocation and provides a ~5x speedup for buffer conversions.

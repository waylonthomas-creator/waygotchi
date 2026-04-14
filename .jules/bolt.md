## 2026-04-14 - Optimize _888_to_565 byte concatenation in fb.py
**Learning:** Found O(N^2) byte string concatenation bottleneck inside `_888_to_565` in `fb.py`. Also replacing `int.to_bytes` with direct bitwise byte assignment improves performance.
**Action:** Use pre-allocated `bytearray` when dealing with large amount of byte conversions inside loops to prevent memory reallocation and copy overhead.

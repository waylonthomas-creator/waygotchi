## 2026-05-18 - [Python Byte Concatenation Bottleneck]
**Learning:** Using `b += ...` inside loops for large byte sequences causes O(N^2) memory reallocation overhead in Python, heavily impacting performance for UI pixel conversions.
**Action:** Always pre-allocate memory using `bytearray` and assign directly by index when constructing large buffers inside loops.

## 2024-05-24 - Avoid O(N^2) Byte Concatenation in Python
**Learning:** In `pwnagotchi/ui/hw/libs/fb/fb.py`, pure Python byte string concatenation (`b += ...`) inside a loop causes O(N^2) memory reallocation overhead, creating a significant performance bottleneck for pixel conversion when numpy is not available.
**Action:** Always pre-allocate memory using `bytearray` and use direct index assignment with bitwise logic (`b[idx] = val & 0xFF`) instead of `int.to_bytes` inside large loops for high-performance byte manipulation.

## 2026-06-18 - Pre-allocating byte buffers in Python
**Learning:** In Python, doing byte string concatenation `b += ...` inside a tight loop causes O(N^2) memory reallocation overhead. This is a severe bottleneck for large framebuffers like in `pwnagotchi/ui/hw/libs/fb/fb.py`. Also, using `int.to_bytes` in loops is slow compared to direct bitwise operations.
**Action:** Always pre-allocate memory using `bytearray` and use direct index assignment with bitwise logic for high-performance byte manipulation in pure Python fallbacks.

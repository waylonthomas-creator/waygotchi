## YYYY-MM-DD - [Title]
**Learning:** [Insight]
**Action:** [How to apply next time]

## 2024-05-12 - Optimize _888_to_565 string concatenation
**Learning:** In Pwnagotchi's framebuffer (`fb.py`), `_888_to_565` is used as a pure Python fallback for NumPy. Using string concatenation (`b += ...`) inside the loops converting a large screen buffer to RGB565 format caused massive O(N^2) memory reallocation overhead.
**Action:** Use pre-allocated `bytearray` and direct index assignment with bitwise ops (`val & 0xFF`, `val >> 8`) instead of `int.to_bytes` to improve performance drastically (~27x speedup for 800x480 resolution) without external dependencies.

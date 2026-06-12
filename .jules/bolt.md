## 2024-05-20 - [O(N^2) Bottleneck in Pure Python FB Conversions]
**Learning:** The pure Python fallback for framebuffer color conversion (`_888_to_565`) uses O(N^2) byte concatenation (`b += ...`) and `int.to_bytes` in a tight loop, taking ~30s for a full screen image. This is a severe bottleneck when numpy is unavailable on embedded devices.
**Action:** Always use pre-allocated `bytearray` with direct bitwise index assignments (`b[j] = val & 0xFF`, `b[j+1] = val >> 8`) for high-performance byte packing inside loops, which runs >100x faster (~0.25s).

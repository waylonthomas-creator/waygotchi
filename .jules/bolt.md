## 2026-05-28 - Framebuffer pure-Python color conversion bottleneck
**Learning:** String concatenation and int.to_bytes in a loop inside _888_to_565 (pure Python fallback) is an O(N^2) performance bottleneck for framebuffer updates when numpy is not available.
**Action:** Use pre-allocated bytearray and direct bitwise assignment (val & 0xFF, val >> 8) to vastly improve array construction time, maintaining UI responsiveness on embedded hardware.

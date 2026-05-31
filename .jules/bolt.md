## 2024-05-15 - Framebuffer Color Conversion Bottleneck
**Learning:** The fallback function `_888_to_565` in pure Python relies on byte string concatenation inside a loop, causing O(N^2) memory reallocation overhead. This becomes a severe bottleneck (taking ~47 seconds for a single 800x600 frame) since `numpy` is no longer a project dependency.
**Action:** Use pre-allocated `bytearray` and direct bitwise masking to construct binary data iteratively without `int.to_bytes` or byte concatenation overhead.

## 2024-04-22 - [Avoid O(N^2) Reallocation in Framebuffer pure-Python Fallbacks]
**Learning:** Pure Python framebuffer conversions (e.g., `_888_to_565` fallback) relying on loop-based byte string concatenation (`b += ...`) suffer from massive O(N^2) memory reallocation overhead for larger images or repeating elements, severely impacting UI responsiveness on embedded hardware.
**Action:** Always pre-allocate memory using `bytearray` when processing large pixel buffers natively, and use index assignment or `struct.pack_into` rather than repeated string appending.

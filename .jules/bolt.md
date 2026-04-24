
## 2024-05-24 - Pre-allocate byte buffers for framebuffer image processing
**Learning:** Pure Python implementations of UI rendering operations like RGB888 to RGB565 conversion (`_888_to_565`) can bottleneck significantly when repeatedly appending to `bytes` (`b += ...`) inside a large loop, causing O(N^2) memory reallocation overhead.
**Action:** Always pre-allocate memory using `bytearray` sized exactly for the required output size, and use `struct.pack_into` (or direct slicing/assignment) to construct large binary buffers sequentially, especially in core routines that run frequently without numpy.

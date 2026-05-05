## 2024-05-05 - Avoid O(N^2) byte string concatenation loops for large buffers
**Learning:** During image format conversion in Python, repeatedly appending to a byte string (`b += ...`) inside a loop over a large buffer (like framebuffer raw bytes) creates O(N^2) overhead due to constant memory reallocation.
**Action:** Always pre-allocate memory using `bytearray` when constructing large byte buffers in Python, and use direct index assignments or slice assignments instead.

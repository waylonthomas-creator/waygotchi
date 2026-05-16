## 2024-05-16 - Framebuffer Update String Concatenation Overhead
**Learning:** In Python, using string concatenation (`b += ...`) and `int.to_bytes` in a tight loop to encode framebuffers creates massive memory reallocation overhead, especially on embedded systems.
**Action:** Always use pre-allocated `bytearray` and direct index assignment with bitwise logic (e.g. `val & 0xFF`, `val >> 8`) when converting large buffers for display drivers.

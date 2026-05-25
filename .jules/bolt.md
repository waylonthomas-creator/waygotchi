## 2026-05-25 - [Framebuffer O(N^2) Concatenation Overhead]
**Learning:** Using Python byte string concatenation (`b += ...`) inside a loop for constructing large byte buffers (like framebuffer pixels) causes O(N^2) memory reallocation overhead, which severely degrades performance on embedded hardware.
**Action:** Always pre-allocate memory using `bytearray` and assign values via index instead of using string concatenation when generating large dynamic buffers.

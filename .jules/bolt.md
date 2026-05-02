## 2024-05-02 - Optimize framebuffer RGB to 565 conversion
**Learning:** Using `b += ...` byte string concatenation inside a loop to construct a large binary buffer (like an image framebuffer) introduces massive O(N^2) memory reallocation overhead. In our benchmark, a 1024x768 framebuffer conversion took ~145s with concatenation, versus ~0.5s with a pre-allocated `bytearray`.
**Action:** When performing byte-level transformations to construct large buffers in Python, always pre-allocate a `bytearray` of the target size and use direct index assignment rather than incrementally appending bytes.

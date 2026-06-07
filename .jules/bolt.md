## 2024-05-15 - [Optimize Framebuffer Conversion]
**Learning:** In the absence of `numpy`, pure Python byte string concatenation inside tight loops (like in framebuffer conversions) becomes a severe O(N^2) performance bottleneck on embedded hardware.
**Action:** Always pre-allocate a `bytearray` and use direct index assignment combined with bitwise operations to construct large byte buffers instead of using `+=` or `int.to_bytes`.

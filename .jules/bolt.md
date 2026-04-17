## 2026-04-17 - [O(N^2) byte concatenation pattern]
**Learning:** O(N^2) byte string concatenation (`b += ...`) is a common bottleneck when constructing large buffers. Pre-allocating a `bytearray` and using `struct.pack_into` provides a substantial performance boost (up to 20x).
**Action:** Use `bytearray` pre-allocation and `struct.pack_into` or array item assignment to eliminate O(N^2) byte concatenation overhead in loops when parsing or generating image/binary data.

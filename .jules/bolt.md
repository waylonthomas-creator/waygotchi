## 2024-05-27 - Fast bytearray creation for framebuffer processing
**Learning:** In `pwnagotchi/ui/hw/libs/fb/fb.py`, when applying the pure-Python fallback `_888_to_565`, appending bytes to `b''` via `int.to_bytes()` inside a loop performs poorly because of excessive O(N^2) memory reallocation and function overhead.
**Action:** Using a pre-allocated `bytearray` with direct index assignment (`b[j] = val & 0xFF`, `b[j+1] = val >> 8`) instead of byte string concatenation inside the loop offers around a ~16x speedup.

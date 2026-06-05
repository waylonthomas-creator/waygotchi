
## 2024-05-18 - Framebuffer pure Python fallback optimization
**Learning:** The removal of `numpy` as a dependency means pure Python fallbacks (like `_888_to_565` in `fb.py`) are now on the critical execution path for UI rendering. O(N^2) string concatenation and `int.to_bytes` inside tight loops cause significant performance overhead on embedded hardware.
**Action:** Always pre-allocate memory using `bytearray` and perform direct bitwise assignments (`b[idx] = val & 0xFF`, `b[idx+1] = val >> 8`) instead of relying on string concatenation or `int.to_bytes` for high-performance Python buffer manipulations.

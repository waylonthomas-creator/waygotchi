## 2023-10-27 - [Optimize pure Python 888 to 565 conversion]
**Learning:** Found pure python `_888_to_565` inside `pwnagotchi/ui/hw/libs/fb/fb.py` that concatenates bytes `b += ...` which is O(N^2) time complexity. Using `bytearray` memory pre-allocation and slice/index assignment improves performance significantly without numpy dependency.
**Action:** Replace byte concatenation loop with a pre-allocated `bytearray` loop.

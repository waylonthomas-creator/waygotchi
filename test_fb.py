import time
import os

def _888_to_565_old(bt):
    b = b''
    for i in range(0, len(bt), 3):
        b += int.to_bytes(bt[i] >> 3 << 11 | bt[i + 1] >> 2 << 5 | bt[i + 2] >> 3, 2, 'little')
    return b

def _888_to_565_new(bt):
    # Optimize pure Python fallback: avoid O(N^2) string concatenation
    # and slow int.to_bytes by pre-allocating bytearray and doing bitwise assignment.
    # Yields significant performance improvement when numpy is unavailable.
    n = len(bt)
    b = bytearray(n // 3 * 2)
    j = 0
    for i in range(0, n, 3):
        val = bt[i] >> 3 << 11 | bt[i + 1] >> 2 << 5 | bt[i + 2] >> 3
        b[j] = val & 0xFF
        b[j + 1] = val >> 8
        j += 2
    return bytes(b)

bt = os.urandom(800 * 480 * 3) # simulate a large image

t0 = time.time()
r1 = _888_to_565_old(bt)
t1 = time.time()
print("Old:", t1 - t0)

t0 = time.time()
r2 = _888_to_565_new(bt)
t1 = time.time()
print("New:", t1 - t0)

assert r1 == r2
print("Outputs match!")

import time
import os

def old_888_to_565(bt):
    b = b''
    for i in range(0, len(bt), 3):
        b += int.to_bytes(bt[i] >> 3 << 11 | bt[i + 1] >> 2 << 5 | bt[i + 2] >> 3, 2, 'little')
    return b

def new_888_to_565(bt):
    n = len(bt) // 3
    b = bytearray(n * 2)
    for i in range(n):
        idx = i * 3
        val = (bt[idx] >> 3 << 11) | (bt[idx + 1] >> 2 << 5) | (bt[idx + 2] >> 3)
        b[i * 2] = val & 0xFF
        b[i * 2 + 1] = val >> 8
    return bytes(b)

bt = os.urandom(800 * 480 * 3) # 800x480 resolution image in 24-bit RGB

start = time.time()
old_res = old_888_to_565(bt)
t1 = time.time() - start

start = time.time()
new_res = new_888_to_565(bt)
t2 = time.time() - start

print(f"Old: {t1:.4f}s")
print(f"New: {t2:.4f}s")
print(f"Speedup: {t1/t2:.2f}x")
assert old_res == new_res

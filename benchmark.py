import time
import os

def _888_to_565_old(bt):
    b = b''
    for i in range(0, len(bt), 3):
        b += int.to_bytes(bt[i] >> 3 << 11 | bt[i + 1] >> 2 << 5 | bt[i + 2] >> 3, 2, 'little')
    return b

def _888_to_565_new(bt):
    length = len(bt)
    out = bytearray((length // 3) * 2)
    j = 0
    for i in range(0, length, 3):
        val = (bt[i] >> 3 << 11) | (bt[i + 1] >> 2 << 5) | (bt[i + 2] >> 3)
        out[j] = val & 0xFF
        out[j + 1] = val >> 8
        j += 2
    return bytes(out)

# Generate a random 800x600 RGB buffer
test_data = os.urandom(800 * 600 * 3)

start = time.time()
res1 = _888_to_565_old(test_data)
time1 = time.time() - start

start = time.time()
res2 = _888_to_565_new(test_data)
time2 = time.time() - start

print(f"Old: {time1:.4f}s")
print(f"New: {time2:.4f}s")
print(f"Match: {res1 == res2}")

## 2026-04-15 - Refactored string concatenation in auto-tune.py
**Learning:** Found string concatenations (`+=`) happening inside an O(N) loop generating HTML inside `auto-tune.py`, leading to O(N^2) memory reallocation. Python's string immutability makes large concatenations inside loops highly inefficient.
**Action:** Always prefer accumulating string fragments into a list and using `"".join(list)` instead of repeated `+=` string concatenation inside loops for HTML or logging construction.

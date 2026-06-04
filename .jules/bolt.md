## 2026-06-04 - Pre-normalize invariant criteria in loops
**Learning:** When filtering lists using invariant criteria (like string matching against a static whitelist list), normalizing the whitelist strings inside the nested loop causes O(N*M) overhead.
**Action:** Pre-normalize the criteria list outside the loop to reduce complexity to O(N+M). This significantly improves performance on embedded hardware like the Pi Zero.

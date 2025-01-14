from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        h = Counter(s)

        return sum(2 if not n % 2 else 1 for n in h.values())
       
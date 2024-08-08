from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum([n*(i//8+1) for i, n in enumerate(sorted(Counter(word).values(), reverse=True))])
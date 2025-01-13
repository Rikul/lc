from collections import Counter

class Solution:

    def __init__(self):
        self.W1 = {}
        self.chars = Counter()

    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
    
        for word in words1:
            self.W1[word] = Counter(word)

        for w in words2:
            for ch in w:
                cnt = w.count(ch)
                self.chars[ch] = max(self.chars[ch], cnt)

        result = []
        for w,x in self.W1.items():
            universal = True
            for ch in self.chars:
                if x[ch] < self.chars[ch]:
                    universal = False
                    break

            if universal:
                result.append(w)
                    
        return result
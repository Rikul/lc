from collections import defaultdict
from typing import List

class Solution:

    def hasAllWords(self, s: str, words: List[str]) -> True:

        wordlen = len(words[0])
        swords = []
        for i in range(0, len(s), wordlen):
            swords.append(s[i:i+wordlen])

        return words == sorted(swords)

        
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        result = []
        words.sort()

        ht_words = defaultdict(int)
        allwords = "".join(words)
        wordslen = len(allwords) 

        for c in allwords:
            ht_words[c] += 1
        
        ht_s = defaultdict(int)
        for c in s[0:wordslen]:
            ht_s[c] += 1

        i = 0
        while True:
            if ht_words == ht_s:
                # Same num of chars.
                if self.hasAllWords(s[i:i+wordslen], words):
                    result.append(i)

            i += 1
            if i + wordslen > len(s):
                break
            else:
                ht_s[s[i-1]] -= 1
                if ht_s[s[i-1]] == 0:
                    del ht_s[s[i-1]]

                ht_s[s[i+wordslen-1]] += 1

        return result
                
if __name__ == "__main__":
    sol = Solution()
    # Example usage:
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    result = sol.findSubstring(s, words)
    print(result)
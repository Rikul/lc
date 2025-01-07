class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        words.sort(key=len)
        result = set()
        for i,smaller_word in enumerate(words):
            for j in range(i+1, len(words)):
                if words[j].find(smaller_word) != -1:
                    result.add(smaller_word)
        
        return list(result)
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result : list[int] = []
        vowels = {'a','e','i','o','u'}
        v_words : list[bool] = [False] * len(words)
        prefix_sums : list[int] = [0] * len(words)

        for i,word in enumerate(words):
            v_words[i] = words[i][0] in vowels and words[i][-1] in vowels

        prefix_sums[0] = 0 + (v_words[0] == True)
        for i in range(1, len(words)):
            prefix_sums[i] = prefix_sums[i-1] + (v_words[i] == True)

        for query in queries:
            cnt = 0
            start = query[0]
            end = query[1]
            cnt = prefix_sums[end] - prefix_sums[start] + (v_words[start] == True)

            result.append(cnt)

        return result

class Solution(object):
    def wordBreak(self, s, wordDict):
        \\\
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        \\\
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [\\]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    subs = dfs(end)
                    for sub in subs:
                        if sub:
                            sentences.append(word + \ \ + sub)
                        else:
                            sentences.append(word)
            memo[start] = sentences
            return sentences

        return dfs(0)
        
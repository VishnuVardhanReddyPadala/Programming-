class Solution(object):
    def fullJustify(self, words, maxWidth):
        \\\
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        \\\
        res = []
        i = 0
        n = len(words)
        
        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line = \\
            num_words = j - i
            if j == n or num_words == 1:
                line = \ \.join(words[i:j])
                line += \ \ * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - sum(len(word) for word in words[i:j])
                space_between = total_spaces // (num_words - 1)
                extra = total_spaces % (num_words - 1)
                for k in range(i, j - 1):
                    line += words[k]
                    line += \ \ * (space_between + (1 if k - i < extra else 0))
                line += words[j - 1]
            res.append(line)
            i = j

        return res
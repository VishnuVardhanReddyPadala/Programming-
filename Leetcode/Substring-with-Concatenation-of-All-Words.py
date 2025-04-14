class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_map = {}
        result = []

        for word in words:
            word_map[word] = word_map.get(word, 0) + 1

        for i in range(word_len):
            left = i
            count = 0
            seen = {}

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_map:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    # More than expected, shrink the window from left
                    while seen[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # Found a valid window
                    if count == num_words:
                        result.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = j + word_len

        return result

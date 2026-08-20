class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        need = {}

        for word in words:
            need[word] = need.get(word, 0) + 1

        ans = []

        for i in range(len(s) - total_len + 1):

            seen = {}

            for j in range(i, i + total_len, word_len):

                word = s[j:j + word_len]

                if word not in need:
                    break

                seen[word] = seen.get(word, 0) + 1

                if seen[word] > need[word]:
                    break

            else:
                if seen == need:
                    ans.append(i)

        return ans

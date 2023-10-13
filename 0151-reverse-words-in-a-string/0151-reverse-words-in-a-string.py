class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip()

        words = s.split()

        reversed_words = reversed(words)

        return " ".join(reversed_words)
        
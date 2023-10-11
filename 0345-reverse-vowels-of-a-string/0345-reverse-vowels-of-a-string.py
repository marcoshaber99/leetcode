class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a':True, 'e':True, 'i':True, 'o':True, 'u':True, 'A':True, 'E':True, 'I':True, 'O':True, 'U':True}

        left = 0
        right = len(s)-1

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]

                left +=1
                right -= 1
            elif s[left] not in vowels:
                left +=1
            elif s[right] not in vowels:
                right -=1
        return "".join(s)

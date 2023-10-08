class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check for common characters by concatenating the strings
        if str1 + str2 != str2 + str1:
            return ""
        
        # Function to find the greatest common divisor (GCD) of integers
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        # Use GCD to find common substring
        return str1[:gcd(len(str1), len(str2))]

        
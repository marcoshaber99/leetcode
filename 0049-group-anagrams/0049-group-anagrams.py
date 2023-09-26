class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize an empty dictionary to hold sorted string -> original string(s) mapping
        anagrams = {}
        
        # Loop through each string in the input list
        for s in strs:
            # Sort each string and use it as a key for the anagram groups
            sorted_s = "".join(sorted(s))
            
            # If the sorted string is not in anagrams, add it with an empty list as its value
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            
            # Append the original string to the corresponding sorted string's list
            anagrams[sorted_s].append(s)
        
        # Return the anagram groups as a list
        return list(anagrams.values())
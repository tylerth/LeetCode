# 1003. Check If Word Is Valid After Substitutions
# Difficulty: Medium

'''
We are given that the string "abc" is valid.

From any valid string V, we may split V into two pieces X and Y such that X + Y (X concatenated with Y) is equal to V.  (X or Y may be empty.)  Then, X + "abc" + Y is also valid.

If for example S = "abc", then examples of valid strings are: "abc", "aabcbc", "abcabc", "abcabcababcc".  Examples of invalid strings are: "abccba", "ab", "cababc", "bac".

Return true if and only if the given string S is valid.
'''

class Solution:
    def isValid(self, S: str) -> bool:
        
        temp = S
        pattern = "abc"
        
        for elem in temp:
            if pattern in temp:
                temp = temp.replace(pattern, "")
        
        if temp == "":
            return True
        else:
            return False
# Problem: 1768. Merge strings Alternitately
# Difficulty: Easy
# Description: You are given two strings word1 and word2. Merge the strings by adding letters in alternating
#   order, starting with word1. If a string is longer than the other, append the additional letters onto the end
#   of the merged string.
#   Return the merged string.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # make a empty string that can be returned as output
        output = ""
        
        # start a loop that runs min(word1_len, word2_len) times.
        end = min(len(word1), len(word2))
        snip = 0
        for index in range(end):
            # each loop grab a letter from each list and add it to the output string.
            output = output + word1[index] + word2[index]
            snip = index + 1
        if len(word1) > snip:
            output = output + word1[snip::]
        elif len(word2) > snip:
            output = output + word2[snip::]
        return output
        
        
        
        
if __name__ == "__main__":
    solution = Solution()
    
    output = solution.mergeAlternately(word1 = "abc", word2= "def") # expect "adbef"
    print(output)
    
    output = solution.mergeAlternately(word1 = "ab", word2= "pqrs") # expect "adbef"
    print(output)
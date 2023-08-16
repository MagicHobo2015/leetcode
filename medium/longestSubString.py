class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pile = "" # string allows join
        maxlength = -1 # just to init this
        string_length = len(s)
        if (string_length < 2):
            return string_length
        for character in list(s):
            current = character
            if (current in pile):
                pile = pile[pile.index(character) + 1:]
            pile = pile + character
            maxlength = max(len(pile), maxlength)
        return maxlength


def main():
    stringChecker = Solution()
    # outPut: 3 because abc has len 3
    string_one = "aabaab!bb"
    should_be = stringChecker.lengthOfLongestSubstring(string_one)
    print(f'Should be: 3, was actually: {should_be}')
    
    # output: 1
    string_two = "bbbbb"
    should_be = stringChecker.lengthOfLongestSubstring(string_two)
    print(f'Should be: 1, was actually: {should_be}')

    # output: 3
    string_three = "pwwkew"
    should_be = stringChecker.lengthOfLongestSubstring(string_three)
    print(f'Should be: 3, was actually: {should_be}')
    
    # output: 1
    string_four = " " # output" 3
    should_be = stringChecker.lengthOfLongestSubstring(string_four)
    print(f'Should be: 1, was actually: {should_be}')
    
    # output: 3
    string_five = "dvdf"
    should_be = stringChecker.lengthOfLongestSubstring(string_five)
    print(f'Should be: 3, was actually: {should_be}')

if __name__ == "__main__":
    main()
def isPalindrome(x):
    # negatives are not because of the -
    if x < 0: return print("False")
    # single digits ARE palindromes
    if x > 0 and x < 10: return print("True")
            # This bit splits into seprate chars
    char_array = [*str(x)]
    # this counts up
    index = 0
    # create reverse iterator to compare to the forward one
    # 
    end_of_list = round(len(char_array)/2)
    print(end_of_list)
    for reverse_index in reversed(range(0, end_of_list)):
        # make sure it match, if they do keep going.
        if char_array[index] == char_array[reverse_index + 1]:
            index += 1
        else:
            return print("False")
    return print("True")
     
isPalindrome(10)
isPalindrome(100)
isPalindrome(123)
isPalindrome(121)
# isPalindrome(202020202020202)
# isPalindrome(34874573838474234234)
# https://leetcode.com/problems/palindrome-number/submissions/

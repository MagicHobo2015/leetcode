# 50. Pow(x,n)
"""
    Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n
    
def main():
    solution = Solution()
    
    x, n = 2.00000, 10
    answer = solution.myPow(x, n)
    print(f'Expected: 1024.0000, Actual: {answer}')
    
    x, n = 2.10000, 3
    answer = solution.myPow(x, n)
    print(f'Expected: 9.26100, Actual: {answer}')
    
    x, n = 2.00000, -2
    answer = solution.myPow(x, n)
    print(f'Expected: 0.25000, Actual: {answer}')
    

if __name__ == "__main__":
    main()
    
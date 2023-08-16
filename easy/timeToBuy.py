# 121. best time to buy and sell stock
# Easy

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        largest_profit, smallest_number = float('-inf'), prices[0]
        
        for price in prices:
            largest_profit = max(largest_profit, price - smallest_number)
            smallest_number = min(smallest_number, price)
        return largest_profit
            
        
def main():
    solution = Solution()
    
    print(float('-inf'))
    prices = [7,1,5,3,6,4]
    answer = solution.maxProfit(prices)
    print(f'Expected: 5, Actually: {answer}')
    
    prices = [7,6,4,3,1]
    answer = solution.maxProfit(prices)
    print(f'Expected: 0, Actually: {answer}')
    
    prices = [2,1]
    answer = solution.maxProfit(prices)
    print(f'Expected: 0, Actually: {answer}')
    
    prices = [3,2,6,5,0,3]
    answer = solution.maxProfit(prices)
    print(f'Expected: 4, Actually: {answer}')
    

if __name__ == "__main__":
    main()
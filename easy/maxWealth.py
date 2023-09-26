# Problem: 1672. Richest Customer Wealth
# Difficulty: Easy

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        # the sum of the list at customer number is wealth
        # init this here so it persists through all loops.
        maximum_wealth = 0
        # loop through all the accounts
        for account in accounts:
            # init this here so it persists through all the amount loops, and resets each account
            total_in_account = 0
            # This is where you tally up the wealth of each account.
            for amount in account:
                # adds each amount
                total_in_account += amount
            # keep the largest amount.
            if total_in_account > maximum_wealth:
                maximum_wealth = total_in_account
        # return the maximum.
        return maximum_wealth
        


def main():
    solution = Solution()

    accounts_input = [[1,2,3],[3,2,1]]  # expected output: 6
    output = solution.maximumWealth(accounts_input)
    print(output)

    accounts_input = [[1,5],[7,3],[3,5]]  # expected output: 10
    output = solution.maximumWealth(accounts_input)
    print(output)

    accounts_input = [[2,8,7],[7,1,3],[1,9,5]] # expected output: 17
    output = solution.maximumWealth(accounts_input)
    print(output)



if __name__ == "__main__":
    main()
    print('Bye, Bye')
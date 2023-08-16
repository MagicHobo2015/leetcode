# 15. 3Sum - MEDIUM
"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution(object):
    def twoSum(self, nums, target, target_index):  
        for outter_number_index, outter_number in enumerate(nums):
            if outter_number_index == target_index:
                continue
            # inside looper
            for inner_number_index, innert_number in enumerate(nums):
                if (outter_number_index == inner_number_index) or (inner_number_index == target_index):
                    continue
                elif outter_number + innert_number == target:
                    return sorted([nums[outter_number_index], nums[inner_number_index], nums[target_index]])


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Approach Two: lets try just two loops. sort the list for 
        #   easy duplicate check.
        nums_sorted = sorted(nums)
        length = len(nums) - 2
        results = []
        answer = []

        for index in range(0, length):
            target = 0 - nums_sorted[index] # 4
            answer.append(self.twoSum(nums_sorted, target, index))
        if answer:
            for thing in answer:
               if thing != None and thing not in results:
                   results.append(thing)
        return results




def main():
    print((0 - -1) + 0 + (-1))
    solution = Solution()
    
    nums = [-1,0,1,2,-1,-4]
    answer = solution.threeSum(nums)
    print(f'Expected:\t [[-1 ,0 ,1], [-1, -1, 2]], \nActual: \t{answer}')
    
    nums = [0,1,1]
    answer = solution.threeSum(nums)
    print(f'Expected: [], Actual: {answer}')
    
    nums = [0,0,0]
    answer = solution.threeSum(nums)
    print(f'Expected: [0, 0, 0], Actual: {answer}')
    
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    answer = solution.threeSum(nums)
    print(f'Expected: [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]],\n Actual: {answer}')
    
    
if __name__ == "__main__":
    main()
    
    
    # # approach One: brute force: timeLimit Exceeded
        # list_to_return = []
        # length_of_nums = len(nums)
        # results = []
        
        # # less than three means its not possible to add three..
        # if length_of_nums < 3: return []
        
        # for x in range(0, length_of_nums):
        #     # first number is x
        #     for y in range(x + 1, length_of_nums):
        #         # second number y
        #         for z in range(y+1, length_of_nums):
        #             num_one, num_two, num_three = nums[x], nums[y], nums[z]
        #             if num_one + num_two + num_three == 0:
        #                 temp = [num_one, num_two, num_three]
        #                 temp = sorted(temp)
        #                 list_to_return.append(temp)
        # for numList in list_to_return:
        #     if numList not in results:
        #         results.append(numList)
        # return results
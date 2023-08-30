# looks for instances of tuples that add to target
"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # outside looper
    for outter_number_index, outter_number in enumerate(nums):
        # inside looper
        for inner_number_index, innert_number in enumerate(nums):
            if outter_number_index == inner_number_index:
                pass
            elif outter_number + innert_number == target:
                return [outter_number_index, inner_number_index]

def main():
    # return [1,2]
    print(twoSum([3,2,4], 6))

    # # return [0,1]
    print(twoSum([2,7,11,15], 9))

    # # return [0,1]
    twoSum([3,3], 6)

    # # return [0,2]
    print(twoSum([3,2,3], 6))

if __name__ == "__main__":
    main()


# t
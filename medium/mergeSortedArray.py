# 88. Merge Sorted Array
# easy

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # going for O(m + n), so one loop
        numbers = nums1[:m]
        main_index = index_one = index_two = 0
        
        # this loops until, one of these 
        while index_one < m and index_two < n:
            num_one, num_two = numbers[index_one], nums2[index_two]
            if num_one < num_two:
                nums1[main_index] = num_one
                main_index += 1
                index_one += 1
            else:
                nums1[main_index] = num_two
                main_index += 1
                index_two += 1
                
        # finish it off if m was bigger
        while index_one < m:
            nums1[main_index] = numbers[index_one]
            index_one += 1
            main_index += 1
            
        # finish it off if n was bigger.
        while index_two < n:
            nums1[main_index] = nums2[index_two]
            index_two += 1
            main_index += 1
        return # return nothing!


def main():
    solution = Solution()
    
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    solution.merge(nums1, m, nums2, n)
    print(f'Expected:\t[1,2,2,3,5,6]')
    print(f'Actual:\t{nums1}')
    
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    
    solution.merge(nums1, m, nums2, n)
    print(f'Expected:\t[1]')
    print(f'Actual:\t{nums1}')
    
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    
    solution.merge(nums1, m, nums2, n)
    print(f'Expected:\t[1]')
    print(f'Actual:\t{nums1}')
    
    
if __name__ == "__main__":
    main()
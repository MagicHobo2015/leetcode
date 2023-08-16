# 217: Contains Duplicate
"""
Given an integer array nums, return true if any value appears at least twice in
the array, and return false if every element is distinct.
"""
import curses
from curses import wrapper


class Solution():
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted_list = sorted(nums)
        for index, number in enumerate(sorted_list):
            if index == (len(nums) - 1): break
            if number == sorted_list[index + 1]:
                return True
        return False
        
        # works But too slow for tests.
        # pile = []
        
        # for num in nums:
        #     if num in pile: return True
        #     else:
        #         pile.append(num)
        # return False

# this is a class for testing leetcode solutions i am making.
class testing():
    def __init__(self, class_to_test ) -> None:
        # fireup curses
        self.parent_screen = curses.initscr()
        self.child_screen = self.parent_screen.subwin(10, 10, 1, 1)
        self.center_screen_x = (curses.COLS - 1) // 2
        self.inner_screen_size = 10
        self.inner_Y, self.inner_X = 4, self.center_screen_x - (self.inner_screen_size // 2)
        curses.start_color()
        curses.noecho()
        curses.curs_set(0)
        self.parent_screen.keypad(True)
        self.testNumber = 0
        self.testing = True
        self.solution = class_to_test
        self.banner = "Welcome To My LeetCode Tester"
        
        # ************************* INSERT TEST DATA HERE *********************
        self.testDataCorrect = ["True", "False", "True", "True"]
        self.testData = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2], [2,14,18,22,22]]
        self.function_to_test = self.solution.containsDuplicate

    def handleInput(self):
            key = self.parent_screen.getkey()

            if key == 'q':
                self.testing = False

    def start(self):
        testNumber = 0
        
        # this piles all the output into an iterable.
        answer = [self.function_to_test(x) for x in self.testData]
        answer_iter = iter(answer)
        
        
        while self.testing:
            output = next(answer_iter, "End Of Iterator")
            results_txt = f'Actual Answer:\t {output}'
            test_message = f'Test Number: {testNumber + 1}'

            # self.screen.box()
            # self.screen.addstr(1, (self.center_screen - len(self.banner) // 2), self.banner)
            # self.screen.addstr(3, 2, test_message)
            # self.screen.addstr(3, self.center_screen - 3, 'Results')
            
            self.child_screen.box()
            self.child_screen.addstr(0, 0, results_txt)
            self.child_screen.refresh()
            # second window here.
            # self.screen.addstr(4, 2, results_txt)
            self.handleInput()
            testNumber += 1
            self.parent_screen.refresh()
            self.parent_screen.clear()
            




    # this cleans up all the curses stuff.
    def cleanExit(self) -> None:
        self.parent_screen.keypad(False)
        curses.curs_set(1)
        curses.echo()
        # closes out curses
        curses.endwin()

    
# ****************** DRIVER CODE **************************** #

def main():
    solution = Solution()
    test_object = testing(solution)
    test_object.start()
    test_object.cleanExit()


    nums = [1,2,3,1]
    # answer = solution.containsDuplicate(nums)
    # print(f'Expecting: True, Got: {answer}')

# if youre running this as a program, then start main
if __name__ == "__main__":
    main()

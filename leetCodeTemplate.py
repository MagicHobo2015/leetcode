# Name:
# Difficulty:
# URL: 
# Contact: Joshua.Land6@Gmail.com

# imports for testClass
import curses
import sys
from time import perf_counter
from curses import panel

# ****************** CHANGE THIS **********************************************
from threeSum import Solution

class Test:
    def __init__( self ) -> None:
        # feels wrong but works.
        self.solution = Solution()
        
        # ******************************** CHANGE THIS TOO ********************
        
        self.function_to_test = self.solution.threeSum # add the function name here
        
        self.valid_input = [[-1,0,1,2,-1,-4],
                            [0,1,1],
                            [-1,0,1,2,-1,-4,-2,-3,3,0,4]]   # this is an array of valid input
        
        self.expected_output = ["[-1 ,0 ,1], [-1, -1, 2]",
                                "[]",
                                "[[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]"]   # output you expect, needs to be the same length as valid_input
        
        # **********************************************************************

        self.messages = { 
                         "welcome" : "Welcome To My LeetCode Tester",
                         "next" : "*-- press Enter to view next Results --*",
                         "end" : "*-- Final Results.. --*",
                         "quit" : " *-- Press q to quit --* ",
                         "results" : "Results"
                         }
        self.measurments = {
            "origin_x" : 0, "origin_y" : 0,
            "width" : 80,
            "banner_height" : 4,
            "lower_window_height" : 12,
            "center_x" : 80 // 2,
            "welcome_y" : 2,
            "lower_y" : 4
                            }

        self.createWindows()


    def prepTest(self):
        curses.start_color()
        # dont show what i type
        curses.noecho()
        # hide the cursor
        curses.curs_set(0)
        # init the keyboard
        self.stdscr.keypad(True)


    def createWindows(self):
        # init curses
        self.stdscr = curses.initscr()
        self.prepTest()
    
        # create the windows
        self.banner_window = curses.newwin(self.measurments["banner_height"],
                                           self.measurments["width"],
                                           self.measurments["origin_y"],
                                           self.measurments["origin_x"] )
        
        self.lower_window = curses.newwin(self.measurments["lower_window_height"], self.measurments["width"], 4, 0 )
    
        # need panels to hold the windows.
        self.parent_window_panel = panel.new_panel(self.banner_window)
        self.lower_window_panel = panel.new_panel(self.lower_window)
    
        # set the borders as id like them.
        self.banner_window.border("#", "#", "#", " ", "#", "#", "#", "#")
        self.lower_window.border("#", "#", "~", "#", "#", "#", "#", "#")
    
        self.update_screen()
    
        self.banner_window.addstr(1, self.measurments["center_x"] - (len(self.messages['welcome']) // 2), self.messages['welcome'])
        self.banner_window.addstr(3, self.measurments["center_x"] - len(self.messages["results"]) // 2, self.messages["results"] )

    def beginTest(self):
        test_number = 0 
        self.testing = True
    
        answers = []
        times = []
        
        
        for array_to_test in self.valid_input:
            stamp_one = perf_counter()
            answer = self.function_to_test(array_to_test)
            stamp_two = perf_counter()
            
            times.append(stamp_two - stamp_one)
            answers.append(answer)

        total_tests = len(answers)
        
        while self.testing:
            remaining_tests = total_tests - test_number + 1
            
            test_message = f'Test Number: {test_number + 1}'
            self.banner_window.addstr(3, 2, test_message)
            total_tests_message = f'Total Test: {total_tests}'
            
            # input, expected, actual, time
            input_message = f'Input: \t{ self.valid_input[test_number] }'
            self.lower_window.addstr(1, 2, input_message)

            expected = f'Expected: \t{ self.expected_output[test_number] }'
            self.lower_window.addstr(3, 2, expected)

            actual = f'Actual:\t { answers[test_number] }'
            self.lower_window.addstr(5, 2, actual)
            
            big_float = times[test_number]
            time = f'It took:\t {(big_float):.6f} Seconds to run this test.'
            self.lower_window.addstr(7, self.measurments["center_x"], time )
            
            self.lower_window.addstr(10, self.measurments["center_x"] - len(self.messages["quit"]) // 2, self.messages["quit"] )
            
            time = f'Test ran in { times } Seconds'
            
            if test_number < total_tests - 1:
                test_number += 1
                self.lower_window.addstr(9, self.measurments["center_x"] - len(self.messages["next"]) // 2, self.messages["next"])
            elif test_number == total_tests -1:
                # change the bottom message
                # move cursor and clear 
                self.lower_window.move(9, 0)
                self.lower_window.clrtobot()
                # replace what we cleared.
                self.lower_window.border("#", "#", "~", "#", "#", "#", "#", "#")
                self.lower_window.addstr(10, self.measurments["center_x"] - len(self.messages["quit"]) // 2, self.messages["quit"] )
                self.lower_window.addstr(9, self.measurments["center_x"] - len(self.messages["end"]) // 2, self.messages["end"])
            else:
                pass               

            self.update_screen()
            self.handleInput()

    def update_screen(self):
        panel.update_panels()
        curses.doupdate()  

    # put console back to normal
    def cleanExit(self):
        # ignore keyboard input
        self.stdscr.keypad(False)
        # show the cursor 
        curses.curs_set(1)
        # show whats typed.
        curses.echo()
        # close, windows
        curses.endwin()


    def handleInput(self):
        # checks for quit
        key = self.banner_window.getkey()

        if key == 'q':
            self.testing = False
            self.cleanExit()



def main():
    # this will build test obj, and solution obj.
    test = Test()
    test.beginTest()
    test.cleanExit()
    pass

if __name__ == "__main__":
    main()
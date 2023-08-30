# *************************************************************************** #
#                                                                             #
# Author: Joshua Land                                                         #
# Description: This is a program intended to help me learn algorithms better. #
#       As such we are going to implement visual versions of these algos.     #
#                                                                             #
# *************************************************************************** #

import pygame as pg
from random import randint, shuffle
from time import sleep
import colorsys

class AlgoMagic:
    
    def __init__(self) -> None:
        self.resolution = (2000, 1024)
        pg.init()
        self.screen = pg.display.set_mode(self.resolution, pg.RESIZABLE)
        pg.display.set_caption(' Algorithm Magic ')
        # need this to limit frame rate.
        self.clock = pg.time.Clock()
        self.running = False
        
    def start(self) -> None:
        self.running = True
        
        # create all the bars, but dont draw them here.
        bar_handler = Bar_Handler(self.screen)
        bar_handler.createBars()
        
        og_array = bar_handler.bars
        sorted_array = []
        
        # Main Loop happens here.
        while self.running:
            # clean the screen
            self.screen.fill("black")
            
            # changes should happen here.

            # selection sort
            og_index = 0
            current = og_array[0]
            
            for bar in og_array[og_index:]:
                print(f'Bar Height is: {bar.rect.height}')
                print(f'Current Height: {current.rect.height}')
                if bar.rect.height < current.rect.height:
                    print(f'Swapping bar with current')
                    current = bar
            print(f'Increasing og_index from: {og_index}')
            og_index += 1
            print(f'To: {og_index}')
            sorted_array.append(current)
            current_index = sorted_array.index(current)
            sorted_array[current_index].id = current_index
            print(f'Current ID: {current.id}, Switching ID: {current_index}')
            print(f'Should Grow by one each Time: {len(sorted_array)}')
            

            bar_handler.draw_all()
            # check for exit
            self.handleEvents()
            # show the new changes.
            pg.display.flip()
            # limits frame rate for consistent speeds across devices.
            self.clock.tick(60)

        # clean up
        pg.quit()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
# ************************************ END ALGO MAGIC CLASS *******************


# ************************************************** BAR CLASS ****************
# Bar class, each one comes out a different color.
        # things to edit
class Bar:
    hue = .000# 0.0
    increase = 0.009
    def __init__( self, rect: pg.Rect, id: int ) -> None:
        self.rect = rect
        self.id = id
        self.color = self.set_next_color()


    def set_next_color(self):
        (r, g, b) = colorsys.hsv_to_rgb(Bar.hue, 1.0, 1.0)
        R, G, B = int(255 * r), int(255 * g), int(255 * b)
        Bar.hue += Bar.increase
        return pg.Color(R, G, B)


    def move(self, x_coord: int ) -> None:
        temp = self.rect.centerx
        self.rect.centerx = x_coord


    def draw(self, screen: pg.surface) -> None:
        screen.fill( self.color, self.rect )
# *********************************************** END BAR CLASS ***************


# ******************************** ***************** ********* BAR HANDLER ****
class Bar_Handler:
    def __init__(self, screen: pg.surface) -> None:
        self.bars = []
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.bar_width = 1 * 20 # 20 is a scaler, change in steps of 10. <---------- **SCALER FOR BARS WIDTH**
        self.num_of_bars = (self.screen_width // self.bar_width)

    def createBars(self) -> None:
        # makes enough bars to fill the screen,
            # it makes them in order though so need to randomize
        for number in range(0, self.num_of_bars):
            left = self.bar_width * (number + 1)
            height = (number + 1) * 10 # <-------------------------- **SCALER FOR BAR HEIGHT
            _id = number # id is index.
            top = self.screen_height - height
            rect = pg.Rect(left, top, self.bar_width, height, )
            new_bar = Bar(rect, _id)
            # print( f'Left: { left } \n Top: { top } \n _id: { _id }')
            self.bars.append( new_bar )
        # now that the list is made we need to shuffle it
        self.shuffle_the_list()


    def shuffle_the_list(self):
        shuffle(self.bars)
        index = 0
        for bar in self.bars:
            bar.move(index)
            index += self.bar_width
            

    def move(self, bar_id: int, x_coord: int) -> None:
        current_bar = self.bars[bar_id]
        current_bar.move(x_coord)


    def draw_all(self) -> None:
        for bar in self.bars:
            bar.draw(self.screen)
# ************************************************************ END BAR HANDLER*

# SELECTION SORT SELECTION SORT SELECTION SORT SELECTION SORT SELECTION SORT **
# Selection Sort Works by moving the minimum element in each pass to a new array
#   The complexity is O(n^2), So not good as lists get longer.
class SelectionSort:
    def __init__( self, array_to_sort ) -> None:
        self.og_array = array_to_sort
        self.sorted_array = []
        
    def sort_me(self) -> list:
        while len(self.og_array) > 1:
            for bar in self.og_array:
                smallest = self.og_array[0]
                for number in self.og_array:
                    if number.id < smallest.id:
                        smallest = number
                self.sorted_array.append(smallest)
                self.og_array.pop(smallest)
                
    def align_to_index(self):
        for bar in self.sorted_array:
            bar.move(bar.id)

        

        
    
        



# ***************************************************************** DRIVER CODE 
# Dont think the decorator is needed but trying to work with them more.
@staticmethod
def main():
    algoMagic = AlgoMagic()
    algoMagic.start()
    

# this is so you can run this as a program.
if __name__ == "__main__":
    main()

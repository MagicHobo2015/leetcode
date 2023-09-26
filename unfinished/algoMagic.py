# *************************************************************************** #
#                                                                             #
# Author: Joshua Land                                                         #
# Description: This is a program intended to help me learn algorithms better. #
#       As such we are going to implement visual versions of these algos.     #
#                                                                             #
# *************************************************************************** #

# these are all for different classes, so when Split to separate files makes sure
# to grab the ones needed for each class.
import pygame as pg
from random import randint, shuffle
from math import floor
from time import sleep
import colorsys

# AlgoMagic is designed to only have one instance at a time.
# more than one instance at a time may result in unexpected behavior.
class AlgoMagic:
    # some class attributes, we dont need individual copies of all these.
    # WARNING ALTERING ANY OF THESE WILL CHANGE THEM FOR ALL INSTANCES OF THIS CLASS
    RESOLUTION = (2000, 2000) # length and width of the screen
    WINDOW_TITLE = 'Algorithm Magic'
    BUTTON_COLOR_LIGHT = pg.Color(164, 66, 245) # normal button color
    BUTTON_COLOR_DARK = pg.Color(65, 23, 99)   # Color When hovering over a button
    BUTTON_TXT_COLOR = pg.Color(255, 255, 255) # Button Txt Color.

    # get pygame ready, fire up the main window.
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(self.RESOLUTION, pg.RESIZABLE)
        pg.display.set_caption(self.WINDOW_TITLE)
        self.font = pg.font.SysFont("ariel", 36)
        # need this to limit frame rate.
        self.clock = pg.time.Clock()
        self.sorter = None
        self.running = False
        self.menu = {}


    def start(self) -> None:
        # makes all the buttons
        self.createButtons()
        # create all the bars, but dont draw them here.
        self.bar_handler = Bar_Handler(self.screen)
        self.bar_handler.createBars()
        # create the sorting objects here.
        self.sorter = SelectionSort(self)
        # Main Loop happens here.
        self.running = True # sentinal for mainGameLoop.
        while self.running:
            # clean the screen
            self.screen.fill("black")
            
            # changes should happen here.
            self.bar_handler.draw_all()
            # check for exit
            self.handleEvents()
            # show the new changes.
            pg.display.flip()
            # limits frame rate for consistent speeds across devices.
            self.clock.tick(60)
        # clean up
        pg.quit()

    # happens each loop right before flip.
    def handleEvents(self):
        # grab mouse position.
        mouse_pos = pg.mouse.get_pos()
        # grab and check event queue
        for event in pg.event.get():
            # leave when the user wants to leave.
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONUP:
                self.sorter.start_sorting()

        # change the sort button color when you hover.
        if mouse_pos[0] > 100 and mouse_pos[0] < 200 and mouse_pos[1] > 100 and mouse_pos[1] < 200:
            # switch the button color. Hovering.
            self.button_color = self.BUTTON_COLOR_DARK
        else:
            # here youre not over the button.
            self.button_color = self.BUTTON_COLOR_LIGHT

    def createButtons(self):
        words_for_buttons = ["Select Sort", "Randomize", "Sort"]
        
        # make a light and a dark button for each word in the buttons list.
        for word in words_for_buttons:
            lght_drk = self.button_maker(word)
            self.menu = {word : lght_drk}


    # this makes one button with txt as the word, it handles spacing etc. returns one light button and one dark
    #   This way it can change with hover.
    def button_maker(self, txt):
        button_cushion = .1 # makes buttons look good
        txt_color = pg.Color(255, 255, 255, 255)
        light_color = pg.Color(57, 196, 94)
        dark_color = pg.Color(24, 84, 40)
        font_name = "arial"
        font = pg.font.SysFont(font_name, 36)
        button_txt = font.render(txt, True, txt_color) # make white text
        button_txt_rect = button_txt.get_rect()
        # make the button 20% larger.
        button_rect = pg.Rect(100, 100, button_txt_rect.width + (button_txt_rect.width * .2),
                            button_txt_rect.height + (button_txt_rect.height * .2))

        button_surface_lght = pg.Surface((button_rect.width, button_rect.height), pg.SRCALPHA) # creates the surface
        button_surface_drk = button_surface_lght.copy()

        # Color the buttons
        button_surface_lght.fill(light_color)
        button_surface_drk.fill(dark_color)
        
        # add the txt
        button_surface_lght.blit(button_txt, (button_txt_rect.width * .1, 0))
        button_surface_drk.blit(button_txt, (button_txt_rect.width * .1, 0))
        return [button_surface_lght, button_surface_drk]
        

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
            rect = pg.Rect(left, top, self.bar_width, height )
            new_bar = Bar(rect, _id)
            # print( f'Left: { left } \n Top: { top } \n _id: { _id }')
            self.bars.append( new_bar )
        # now that the list is made we need to shuffle it
        self.shuffle_the_list()

    # I create them in order so we have to shuffle them after
    #  Also useful when I show multiple
    def shuffle_the_list(self):
        shuffle(self.bars)
        self.move_all()

    def swap(self, index_one: int, index_two: int):
        if index_one == index_two:
            return
        # this should swap positions of the bars. Also need to move them
        self.bars[index_one], self.bars[index_two] = self.bars[index_two], self.bars[index_one]
        # move the bars to match thier new index.
        self.bars[index_one].move(index_one * self.bar_width)
        self.bars[index_two].move(index_two * self.bar_width)
        
            
    def move_all(self):
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

# _________________________________________________________________________________________________SELECTION SORT_________________________
# a class to sort list in place. For this to show Im going to require a pg object.
class SelectionSort:
    def __init__(self, algoMagic: AlgoMagic) -> None:
        self.program = algoMagic
        self.list_to_sort = self.program.bar_handler.bars
    
    def start_sorting(self):
         # Selection Sort **********************~----> SELECTION SORT IMPLEMENTATION HERE.
        for i in range(len(self.list_to_sort)):
            min_index = i
            for j in range(min_index + 1, len(self.list_to_sort)):
                if self.list_to_sort[min_index].id > self.list_to_sort[j].id:
                    min_index = j
            self.program.bar_handler.swap(min_index, i)
            # this draws bar_handler.bars
            self.program.bar_handler.draw_all()
            # need to show it working
            pg.display.flip()
            self.program.screen.fill("black")
            self.program.clock.tick(60)
            sleep(.25)



# ***************************************************************** DRIVER CODE 
# Dont think the decorator is needed but trying to work with them more.
@staticmethod
def main():
    algoMagic = AlgoMagic()
    algoMagic.start()
    

# this is so you can run this as a program.
if __name__ == "__main__":
    main()

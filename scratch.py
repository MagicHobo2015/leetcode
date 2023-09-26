






























































# import pygame as pg
# from pygame import sprite

# def main():
#     # start up pygame
#     pg.init()
#     # start the screen.
#     screen = pg.display.set_mode((2000, 2000))
#     screen.fill("black")

#     clock = pg.time.Clock()

#     buttons = button_maker("Buttons")
    
    
#     button_One = screen.blit(buttons[0], (100, 100))
    
#     button_two = screen.blit(buttons[1], (100, 300))
    
#     button_rects = [ button_One, button_two ]

#     running = True
#     while running:

#         pg.display.flip()
#         mouse = pg.mouse.get_pos() # [x, y]
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 running = False
#             elif event.type == pg.MOUSEBUTTONUP:
#                 for button in button_rects:
#                     if button.collidepoint(event.pos):
#                         print(f'Clicked Button: {button}')
#         clock.tick(60)

#     pg.quit()

# def button_maker(txt):
#     button_cushion = .1 # makes buttons look good
#     txt_color = pg.Color(255, 255, 255, 255)
#     light_color = pg.Color(57, 196, 94)
#     dark_color = pg.Color(24, 84, 40)
#     font_name = "arial"
#     font = pg.font.SysFont(font_name, 36)    
#     button_txt = font.render(txt, True, txt_color) # make white text
#     button_txt_rect = button_txt.get_rect()
#      # make the button 20% larger.
#     button_rect = pg.Rect(100, 100, button_txt_rect.width + (button_txt_rect.width * .2),
#                           button_txt_rect.height + (button_txt_rect.height * .2))

#     button_surface_lght = pg.Surface((button_rect.width, button_rect.height), pg.SRCALPHA) # creates the surface
#     button_surface_drk = button_surface_lght.copy()

#     # Color the buttons
#     button_surface_lght.fill(light_color)
#     button_surface_drk.fill(dark_color)
    
#     # add the txt
#     button_surface_lght.blit(button_txt, (button_txt_rect.width * .1, 0))
#     button_surface_drk.blit(button_txt, (button_txt_rect.width * .1, 0))
#     return [button_surface_lght, button_surface_drk]
    
    

    



# if __name__ == "__main__":
#     main()

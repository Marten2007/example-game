import pygame.font

class Button():
    """Class for button"""



    def __init__(self, game_settings, screen, msg):
        """Init button atributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #button atributes - size, color, font
        self.width = 200
        self.height = 50
        self.button_color = (255, 0 , 1)
        self.text_color = (254, 255, 253)
        self.font = pygame.font.SysFont(None, 46)
        #build the button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #prepare grafical text
        self.prepare_msg(msg)


    def prepare_msg(self, msg):
        """Convert text messae to grafics and center with button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

   
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
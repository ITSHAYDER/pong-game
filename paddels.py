
import pygame
pygame.init()
class LeftPaddle:
    def __init__(self, screen_width, screen_height, screen):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        self.color = (255, 255, 255)
        self.height = 50
        self.width = 10
        self.left_x = 1
        self.left_y=screen_height/2
        self.speed=5
        self.rect= pygame.Rect(self.left_x, self.left_y, self.width, self.height)
    def draw_left_paddle(self):
        
        draw_left_paddle= pygame.draw.rect(self.screen, self.color, self.rect)
    def up(self):
        if self.left_y - self.speed > 0:
            self.left_y -= self.speed
            self.rect.y = self.left_y

    def down(self):
        if self.left_y + self.speed < self.screen_height - self.height:
            self.left_y += self.speed
            self.rect.y = self.left_y
class RightPaddle:
    def __init__(self, screen_width, screen_height, screen):
        self.right_x = screen_width-10
        self.right_y=screen_height/2
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        self.color = (255, 255, 255)
        self.height = 50
        self.width = 10
        self.speed=5
        self.rect = pygame.Rect(self.right_x, self.right_y, self.width, self.height)
    def draw_right_paddle(self):
        draw_right_paddle= pygame.draw.rect(self.screen, self.color, self.rect)
    def up(self):
        if self.right_y - self.speed > 0:
            self.right_y -= self.speed
            self.rect.y = self.right_y

    def down(self):
        if self.right_y + self.speed < self.screen_height - self.height:
            self.right_y += self.speed
            self.rect.y = self.right_y
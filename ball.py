import pygame


pygame.init()
class Ball:
    def __init__(self, screen_width, screen_height, screen):
        self.screen = screen
        self.color = (255, 255, 255)
        self.right_score=0
        self.left_score = 0
        self.height = 10
        self.width = 10
        self.x = 200
        self.y = 250
        self.speed = [3.2, 4.5]
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.speed[1] = -self.speed[1]
        elif self.x <= 0 :
            self.left_score += 1
            self.x = self.screen_width / 2
        elif self.x >= self.screen_width:
            self.x = self.screen_width / 2
            self.right_score += 1


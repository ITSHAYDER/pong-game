import pygame, sys
from ball import Ball
from paddels import RightPaddle, LeftPaddle

pygame.init()


class main:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen_width = 500
        self.screen_height = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.caption = pygame.display.set_caption("pong game")
        self.ball = Ball(self.screen_width, self.screen_height, self.screen)
        self.right_paddle = RightPaddle(self.screen_width, self.screen_height, self.screen)
        self.left_paddle = LeftPaddle(self.screen_width, self.screen_height, self.screen)
    def score(self, side, x , y):
        font = pygame.font.Font(None, 16)
        text_surface = font.render(side, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)  # Set the center of the text rect to (400, 450)
        self.screen.blit(text_surface, text_rect)
    def move_paddle(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.right_paddle.up()
        elif keys[pygame.K_DOWN]:
            self.right_paddle.down()
            
        if keys[pygame.K_w]:
            self.left_paddle.up()
        elif keys[pygame.K_s]:
            self.left_paddle.down()
            # Handle down arrow key p
    def coll(self):
            if self.ball.rect.colliderect(self.left_paddle.rect):
                self.ball.speed[0] = abs(self.ball.speed[0])  # change x speed to a positive value

            if self.ball.rect.colliderect(self.right_paddle.rect):
                self.ball.speed[0] = -abs(self.ball.speed[0])
        

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(pygame.Color("BLACK"))
            pygame.draw.line(self.screen, (255, 255, 255), (self.screen_width// 2, 0), (self.screen_width // 2, self.screen_height))
            self.score(str(self.ball.left_score), 450 , 50)
            self.score(str(self.ball.right_score), 50, 50)
            self.ball.move()
            self.ball.draw()
            self.left_paddle.draw_left_paddle()  # draw left paddle
            self.right_paddle.draw_right_paddle()  # draw right paddle
            self.move_paddle()
            self.coll()  # check for collisions
            pygame.display.flip()
            self.clock.tick(60)

            

        pygame.quit()


game = main()
game.start()
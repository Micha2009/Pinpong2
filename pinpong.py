
from random import randint
from pygame import *

win_width = 800
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
#background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))
back =(200, 200, 200)
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height -80:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_Down] and self.rect.y < win_height -80:
            self.rect.y += self.speed
          
pravoa = Player('pesik.png', 30, 200, 4, 50, 150)
levoa = Player('pesik2.png', 520, 200, 4, 50, 150)
masik = GameSprite('', 200, 200, 4, 50, 50)

game = True
clock = time.Clock()
FPS = 600

finish = False

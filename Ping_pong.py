from pygame import *
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-200:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-200:
            self.rect.y += self.speed


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")
FPS = 60
background = transform.scale(image.load('Sahur.jpg'), (win_width, win_height))
clock = time.Clock()
ball = GameSprite('ball.png',300,200,60,60,4)
racket1 = Player('Racketka.png',70,200,30,200,5)
racket2 = Player('Racketka.png',550,200,30,200,5)
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        ball.reset()
        racket1.reset()
        racket2.reset()
        racket1.update_l()
        racket2.update_r()
        display.update()
    clock.tick(FPS)
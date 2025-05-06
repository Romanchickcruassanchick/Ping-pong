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
background = transform.scale(image.load('Beach.jfif'), (win_width, win_height))
clock = time.Clock()
ball = GameSprite('ball.png',300,200,60,60,4)
racket1 = Player('Racketka.png',70,200,80,200,10)
racket2 = Player('Racketka.png',550,200,80,200,10)
game = True
finish = False
speed_x = 10
speed_y = 10
count_r = 0
count_l = 0
font.init()
font1 = font.SysFont("Arial", 28)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:

        window.blit(background,(0,0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        ball.reset()
        racket1.reset()
        racket2.reset()

        racket1.update_l()
        racket2.update_r()
        
        font_r = font1.render(str(count_r),True,(0,255,0))
        font_l = font1.render(str(count_l),True,(0,255,0))

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1

        if ball.rect.x < -10:
            finish = True
            count_r +=1
            
        if ball.rect.x > win_width:
            finish = True
            count_l += 1
            
        
        window.blit(font_l,(200,300))
        window.blit(font_r,(500,300))
        display.update()
    else:
        ball.rect.x = 300
        ball.rect.y = 200
        finish = False
    clock.tick(FPS)

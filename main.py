from pygame import *

window = display.set_mode((700, 500))
background = transform.scale(image.load('background.jpg'),(700,500))
clock = time.Clock()

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (width, height))
       self.speed = speed
       self.rect = self.image.get_rect()
       self.rect.x =  x
       self.rect.y = y
       self.direction = 'left'

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def update_r(self):
        keys  = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:  
            self.rect.x -= self.speed    
        if keys[K_RIGHT] and self.rect.x < 600:  
            self.rect.x += self.speed    
        if keys[K_UP] and self.rect.y > 5:  
            self.rect.y -= self.speed    
        if keys[K_DOWN] and self.rect.y < 400:  
            self.rect.y += self.speed 

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

racket1 = Player('racket.png', 10, 200, 30, 100,  15)
racket2 = Player('racket.png', 660, 200, 30, 100, 15)
ball = Gamesprite('tenis_ball.png', 200, 200, 50, 50, 7) 

speed_x = 5
speed_y = 5
finish = False

font.init()
font1 = font.SysFont('Algerian', 40)
lose1 = font1.render('PLAYER 1 LOSE!', True, (0,0,255))
lose2 = font1.render('PLAYER 2 LOSE!', True, (0,0,255))

game = True
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False   
    racket1.reset()
    racket2.reset()
    ball.reset()

    racket1.update_l()
    racket2.update_r()      
    
     ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y < 0 or ball.rect.y > 450:
            speed_y *= -1

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1

        if ball.rect.x < -50:
            finish = True 
            window.blit(lose1, (200,200))

        if ball.rect.x > 700:
            finish = True 
            window.blit(lose2, (200,200))


            
    clock.tick(60)
    display.update()            


PyGmae
#import modules
import pygame
from pygame.locals import *
import menulib as dm
import random
import time
pygame.init()

keepgoing = True
while keepgoing:
    def text(text,x,y,size,a,b,c):
        pygame.init()
        font = pygame.font.SysFont("monospace", size)
        text = font.render(text, 1, (a,b,c))
        screen.blit(text,(x,y))
        pygame.display.flip()

    #Game Menu
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Catch the Ball: Game Menu")
    screen.fill((255, 255, 0))
    pygame.display.update()
    pygame.key.set_repeat(500,30)

    choose = dm.dumbmenu(screen, [
                            'Start Game',
                            'Instructions',
                            'Quit Game'],70,90,None,50,1.4,(0,0,0),(255,0,0))
    if choose == 0:
        pygame.quit()

    #Game Rules
    if choose == 1:
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Catch the Ball: Game Instructions")
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0,255,0))
        clock = pygame.time.Clock()
        keep_going = True
        while keep_going:
            screen.blit(background, (0,0))
            text("How to Play?",200,0,50,0,0,0)
            text("Use the left and right arrow keys to control the bucket",0,75,20,0,0,0)
            text("Try to catch the balls using the bucket",0,115,20,0,0,0)
            text("For each ball you catch, you will receive one point",0,155,20,0,0,0)
            text("The game will only get harder towards the end",0,195,20,0,0,0)
            text("Remember to set the time limit before you start the game",0,235,20,0,0,0)
            text("Press the Enter key to continue",0,350,20,0,0,255)
            pygame.event.pump()
            clock.tick(1)
            keys = pygame.key.get_pressed()
            for ev in pygame.event.get():
                if ev.type == QUIT or keys[K_RETURN]:
                    keep_going = False
                    pygame.quit()
    #Exiting the Game
    if choose == 2:
        pygame.quit()
        keepgoing = False
        exit()

    #Gameplay
    class ball(pygame.sprite.Sprite):
        def __init__(ball):
            pygame.sprite.Sprite.__init__(ball)
            ball.image = pygame.image.load("ball.png").convert()
            ball.rect = ball.image.get_rect()
            ball.rect.x = random.randint(0,900)
            ball.rect.y = -100
            ball.speed = 4.0
            ball.count = 0
            ball.score = 0

        def main(ball):
            ball.rect.y += ball.speed
            if ball.rect.y > 550:
                hole = pygame.image.load("hole.png").convert()
                background.blit(hole, (ball.rect.x-10,550))
                ball.rect.x = random.randint(0,900)
                ball.rect.y = -100
                ball.speed += 0.07
                ball.count += 1
            if bucket.rect.colliderect(ball.rect) == True:
                ball.score += 1
                X = ball.rect.x
                ball.rect.x = random.randint(0,900)
                ball.rect.y = -200
                ball.speed += 0.07
                ball.count += 1
                for x in range (0,20): 
                    text("+1",X-60,400,50,0,0,255)

    class ball1(pygame.sprite.Sprite):
        def __init__(ball1):
            pygame.sprite.Sprite.__init__(ball1)
            ball1.image = pygame.image.load("ball1.png").convert()
            ball1.rect = ball1.image.get_rect()
            ball1.rect.x = random.randint(0,900)
            ball1.rect.y = -4000
            ball1.speed = 4.5

        def main(ball1):
            ball1.rect.y += ball1.speed
            if ball1.rect.y > 550:
                hole = pygame.image.load("hole.png").convert()
                background.blit(hole, (ball1.rect.x-10,550))
                ball1.rect.x = random.randint(0,900)
                ball1.rect.y = -100
                ball1.speed += 0.06
                ball.count += 1
            if bucket.rect.colliderect(ball1.rect) == True:
                ball.score += 1
                y = ball1.rect.x
                ball1.rect.x = random.randint(0,900)
                ball1.rect.y = -200
                ball1.speed += 0.05
                ball.count += 1
                for x in range (0,20): 
                    text("+1",y-60,400,50,0,0,255)

    class ball2(pygame.sprite.Sprite):
        def __init__(ball2):
            pygame.sprite.Sprite.__init__(ball2)
            ball2.image = pygame.image.load("ball2.png").convert()
            ball2.rect = ball2.image.get_rect()
            ball2.rect.x = random.randint(0,900)
            ball2.rect.y = -8000
            ball2.speed = 5.0

        def main(ball2):
            ball2.rect.y += ball2.speed
            if ball2.rect.y > 550:
                hole = pygame.image.load("hole.png").convert()
                background.blit(hole, (ball2.rect.x-10,550))
                ball2.rect.x = random.randint(0,900)
                ball2.rect.y = -100
                ball.count += 1
            if bucket.rect.colliderect(ball2.rect) == True:
                ball.score += 1
                z = ball2.rect.x
                ball2.rect.x = random.randint(0,900)
                ball2.rect.y = -200
                ball2.speed += 0.05
                ball.count += 1
                for x in range (0,20): 
                    text("+1",z-60,400,50,0,0,255)

    class bucket(pygame.sprite.Sprite):
        def __init__(bucket):
            pygame.sprite.Sprite.__init__(bucket)
            bucket.image = pygame.image.load("bucket.png").convert()
            bucket.rect = bucket.image.get_rect()
            bucket.rect.x = 400
            bucket.rect.y = 488

        def handle_keys(bucket):
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
                bucket.rect.x += 5
            elif key[pygame.K_LEFT]:
                bucket.rect.x -= 5

        def hittingwall(bucket):
            if bucket.rect.x > 1000:
                bucket.rect.x = -150
            elif bucket.rect.x < -200:
                bucket.rect.x = 950

    while True:
        timelimit = int(input("Enter your time limit in seconds(min 30s, max 120s): "))
        if 30 <= timelimit <= 120:
            break
        else:
            print("Time not in range, please try again")
            print(" ")
             
    screen = pygame.display.set_mode((1000, 650))
    pygame.display.set_caption("Catch the Ball!")
    ball = ball()
    ball1 = ball1()
    ball2 = ball2()
    bucket = bucket()

    background = pygame.Surface(screen.get_size()).convert()
    background.fill((255, 255, 255))

    #Gameplay
    clock = pygame.time.Clock()
    keep_going = True
    now = time.time()
    while (time.time()-now) < timelimit:
        clock.tick(100)
        pygame.event.pump()
        for ev in pygame.event.get():
            if ev.type == QUIT:
                keep_going = False

        bucket.handle_keys()
        bucket.hittingwall()
        ball.main()
        ball1.main()
        ball2.main()   

        bucket.update()
        ball.update()
        ball1.update()
        ball2.update()
        screen.blit(background, (0,0))
        screen.blit(ball.image, ball.rect)
        screen.blit(ball1.image, ball1.rect)
        screen.blit(ball2.image, ball2.rect)
        screen.blit(bucket.image, bucket.rect)
        pygame.display.flip()

        text("Score: "+str(ball.score),800,25,30,0,0,0)

        if timelimit-10 > (time.time()-now) > 0:  
            text("Time Left: "+str(int(timelimit-(time.time()-now))),35,25,30,0,0,0)
        if (time.time()-now) >= timelimit-10:
            text("Time Left: "+str(int(timelimit-(time.time()-now))),35,25,30,255,0,0)

        if (time.time()-now) >= timelimit:
            text("Congratulations!",300,225,40,255,0,0)
            text("Your score is: "+str(ball.score),290,275,40,0,0,0)
            text("Out of a total of "+str(ball.count)+" balls",190,325,40,0,0,255)
            time.sleep(10)




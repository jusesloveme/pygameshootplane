import pygame
import sys
from pygame.locals import*
#初始化pygame环境
pygame.init()

#创建一个长宽分别为480/650窗口
screen = pygame.display.set_mode((480, 650))
screen.fill((255,255,255))

#设置窗口标题
pygame.display.set_caption("飞机大战")

enemy=pygame.image.load("images/enemy1.png")
enemy2=pygame.image.load("images/enemy2.png")
enemy3=pygame.image.load("images/enemy3.png")
h=pygame.image.load("images/hero1.png")
bg=pygame.image.load("images/bg1.png")

class Plane:
    def __init__(self):
        self.x=200
        self.y=0
    def move(self,img=enemy,speed=10):
        screen.blit(bg,(0,0))
        screen.blit(img,(self.x,self.y))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == K_d:
                self.x+=speed
            elif event.type == pygame.KEYDOWN and event.key == K_a:
                self.x-=speed
            elif event.type == pygame.KEYDOWN and event.key == K_w:
                self.y-=speed
            elif event.type == pygame.KEYDOWN and event.key == K_s:
                self.y+=speed
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

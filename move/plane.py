#coding:utf-8
import pygame
from pygame.locals import*
import move as bd
#初始化pygame环境
pygame.init()
plane=bd.Plane()

enemy=pygame.image.load("images/enemy1.png")
enemy2=pygame.image.load("images/enemy2.png")
enemy3=pygame.image.load("images/enemy3.png")
h=pygame.image.load("images/hero1.png")
bg=pygame.image.load("images/bg1.png")
      
            
while True:
    #下方写你的代码
    plane.move(enemy,50)
    
    # 更新屏幕内容
    pygame.display.update()

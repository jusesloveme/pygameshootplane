#coding:utf-8
import pygame
from pygame.locals import*
#初始化pygame环境
pygame.init()

#创建一个长宽分别为1400/600窗口
screen = pygame.display.set_mode((1400, 600))
screen.fill((255,255,255))

#设置窗口标题
pygame.display.set_caption("植物大战僵尸")

#加载图片
nut=pygame.image.load("images/plants/TallNut.gif")
zombie=pygame.image.load("images/move/01.png")
bg  =pygame.image.load("images/bgzombie.jpg")
pea=pygame.image.load("images/plants/Peashooter.gif")
flower=pygame.image.load("images/plants/SunFlower.gif")
squash=pygame.image.load("images/plants/Squash.gif")
ice=pygame.image.load("images/plants/IceShroom.gif")
potato=pygame.image.load("images/plants/PotatoMine.gif")

def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()  
                 
#背景(bg)坐标为(0,0)
#坚果(nut1)坐标为(420,250)
#僵尸(zombie)坐标为(1000,100)
#豌豆射手(pea)坐标自己定
#向日葵(flower)坐标自己定
#土豆地雷(potato)坐标自己定
#倭瓜(squash)坐标自己定 
#冰菇(ice)坐标自己定      
       
while True:
    #下方写你的代码             
    screen.blit(bg, (0, 0))
    screen.blit(zombie, (1000, 100))
    screen.blit(flower, (250, 100))
    screen.blit(squash, (250, 150))
    screen.blit(ice, (250, 200))
    screen.blit(pea, (250, 280))
    screen.blit(nut, (420, 250))
    screen.blit(potato, (250, 500))
 
    #更新屏幕内容
    pygame.display.update()
    #处理关闭游戏
    handleEvent()


 

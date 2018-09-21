#coding:utf-8
import pygame
from pygame.locals import*
#初始化pygame环境
pygame.init()

#创建一个长宽分别为1250/650窗口
screen = pygame.display.set_mode((1250, 650))
screen.fill((255,255,255))

#设置窗口标题
pygame.display.set_caption("愤怒的小鸟")

#加载图片
bg  =pygame.image.load("images/bg.png")
pig=pygame.image.load("images/pig.png")
bird=pygame.image.load("images/bird.png")
bird=pygame.image.load("images/bird.png")
s1=pygame.image.load("images/slingshot1.png")
s2=pygame.image.load("images/slingshot2.png")

def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
                  
#背景(bg)坐标——(0,0)
#弹弓1(s1)坐标——(155,305)
#小鸟(bird)坐标——(135,315)
#弹弓2(s2)坐标——(125,300)
#猪(pig)坐标——(1130,315)            
while True:
    #下方写你的代码
    screen.blit(bg, (0, 0))
    screen.blit(s1, (155, 305))
    screen.blit(bird,(135, 315))
    screen.blit(s2, (125, 300))
    screen.blit(pig, (1130, 315))
    
    screen.blit(pig, (820, 365))
    screen.blit(pig, (910, 365))
    screen.blit(pig, (990, 365))
    
    


    #更新屏幕内容
    pygame.display.update()
    #处理关闭游戏
    handleEvent()


 

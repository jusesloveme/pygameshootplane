#coding:utf-8
import pygame
from pygame.locals import*
#初始化pygame环境
pygame.init()

#创建一个长宽分别为800/480窗口
screen = pygame.display.set_mode((800, 480))
screen.fill((255,255,255))

#设置窗口标题
pygame.display.set_caption("捕鱼达人")

#加载图片
net=pygame.image.load("images/net.png")
fish1=pygame.image.load("images/fish10_0.png")
bg  =pygame.image.load("images/bg.jpg")

def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()  
                 
#背景(bg)坐标为(0,0)
#渔网(net)坐标为(300,300)
#鱼(fish1)坐标为(300,100)           
while True:
    #下方写你的代码
    screen.blit(bg, (0, 0))
    screen.blit(fish1, (300, 100))
    screen.blit(net, (300, 300))
    
    #更新屏幕内容
    pygame.display.update()
    #处理关闭游戏
    handleEvent()


 

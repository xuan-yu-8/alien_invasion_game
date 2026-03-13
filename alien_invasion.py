import sys   #使用模块sys来退出游戏；
import pygame #pygame 包括游戏开发的所需功能；
#导入“设置”文件，便于后期对游戏的修改
from settings import Settings   


#创建Pygame 窗口以及响应用户输入：
def run_game():
    pygame.init()  #初始化游戏

#关于设置：
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        #创建屏幕的时候，使用了ai_settings的属性screen_width和screen_height
        (ai_settings.screen_width,ai_settings.screen_height)
    )
    

 #   screen = pygame.display.set_mode((1200,800)) #创建一个屏幕对象
    pygame.display.set_caption("Alien Invasion")

#设置背景色：红、绿、蓝的顺序，当三者的值相同时，屏幕呈现浅灰色：
    bg_color=(230,230,230)


#开始游戏主循环
    while True:
            #设置事件：键盘和鼠标。便于监控，有助于后续玩家操控。
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    #用背景色填充屏幕：因为在循环里面，因此每次循环都要重绘屏幕：
    #    screen.fill(bg_color)

#创建屏幕的时候使用ai_settings来访问背景色
        screen.fill(ai_settings.bg_color) 


#_____从上面开始增加内容，下面是本次框架的一个结尾：
        pygame.display.flip() #展示绘制的屏幕

run_game()



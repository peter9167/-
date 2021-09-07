import pygame as pg
import random

pg.init()

화면가로길이 = 600
화면세로길이 = 800

화면 = pg.display.set_mode((화면가로길이, 화면세로길이))

pg.display.set_caption('생선잡기_게임') #현재 게임 창의 제목 설정

배경이미지 = pg.image.load("img/배경.png") #해당 주소에 있는 이미지 로드(호출). 이 과정에서 Surface라는 파이게임에서 사용되는 이미지를 표현할 수 있는 객체로 반환.
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이)) #새 해상도로 크기 조정 - scale(Surface, (width, height)
화면.blit(배경이미지, (0, 0)) #배경이미지 위치 설정

물고기1 = pg.image.load("img/물고기1.png")
물고기1 = pg.transform.scale(물고기1, (64, 64))
물고기2 = pg.image.load("img/물고기2.png")
물고기2 = pg.transform.scale(물고기2, (64, 64))

스코어바 = pg.image.load("img/스코어바.png")
스코어바 = pg.transform.scale(스코어바, (250, 74)) 

시간바 = pg.image.load("img/시간바.png")
시간바 = pg.transform.scale(시간바, (200, 55))

물고기 = [물고기1, 물고기2]
전체물고기위치 = []

for 가로 in range(70, 520, 90):
    pg.draw.line(화면, (255, 255, 255), (가로, 370), (가로, 화면세로길이-30), 3)
    # 아래 forㄹ를 중첩하지 않아도 되지만, 물고기의 위치 좌표를 얻기 위해 for를 중첩
    for 세로 in range(370, 화면세로길이-30, 80):
        pg.draw.line(화면, (255, 255, 255), (70, 세로), (520, 세로), 3)
        전체물고기위치.append((가로+10, 세로+10))

pg.draw.line(화면, (255, 255, 255), (520, 370), (520, 화면세로길이-30), 3)
pg.draw.line(화면, (255, 255, 255), (70, 화면세로길이-30), (520, 화면세로길이-30), 3)

물고기위치 = random.sample(전체물고기위치, 5)
for 위치 in range(5):
    랜덤물고기 = random.choice(물고기)
    물고기좌표 = 랜덤물고기.get_rect(topleft=(물고기위치[위치][0], 물고기위치[위치][1]))
    화면.blit(랜덤물고기, 물고기좌표)

pg.display.update()

폰트 = pg.font.SysFont('hy얕은샘물m', 30, True)
시작시간 = pg.time.get_ticks()
잡은물고기 = 0

while True :
    경과시간 = round((pg.time.get_ticks() - 시작시간)/1000, 1)
    
    화면.blit(스코어바, (350, 2)) #스코어바 위치 설정
    화면.blit(시간바, (0, 10)) #시간바 위치 설정
    
    시간 = 폰트.render(f'{경과시간} 초', True, (0, 0, 0))
    화면.blit(시간, (60, 28))

    물고기점수 = 폰트.render(f'{잡은물고기} 마리', True, (0, 0, 0))
    화면.blit(물고기점수, (450, 28))

    pg.display.update()

    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()
import pygame as pg

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
화면.blit(물고기1, (100, 400)) #물고기1 위치 설정

물고기2 = pg.image.load("img/물고기2.png")
물고기2 = pg.transform.scale(물고기2, (64, 64)) 
화면.blit(물고기2, (200, 300)) #물고기2 위치 설정

스코어바 = pg.image.load("img/스코어바.png")
스코어바 = pg.transform.scale(스코어바, (250, 74)) 
화면.blit(스코어바, (350, 2)) #스코어바 위치 설정

시간바 = pg.image.load("img/시간바.png")
시간바 = pg.transform.scale(시간바, (200, 55)) 
화면.blit(시간바, (0, 10)) #시간바 위치 설정

pg.display.update()

while True :
    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()
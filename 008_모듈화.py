import pygame as pg
import random
pg.init()

화면가로길이 = 600
화면세로길이 = 800
화면 = pg.display.set_mode((화면가로길이, 화면세로길이))

pg.display.set_caption("생선잡기 게임")
배경이미지 = pg.image.load("img/배경.png")
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이))
화면.blit(배경이미지, (0, 0))

물고기1 = pg.image.load("img/물고기1.png")
물고기1 = pg.transform.scale(물고기1, (64, 64))
물고기2 = pg.image.load("img/물고기2.png")
물고기2 = pg.transform.scale(물고기2, (64, 64))

스코어바 = pg.image.load("img/스코어바.png")
스코어바 = pg.transform.scale(스코어바, (250, 70))

시간바 = pg.image.load("img/시간바.png")
시간바 = pg.transform.scale(시간바, (200, 55))

폰트 = pg.font.SysFont("hy얕은샘물m", 30, True)
시작시간 = pg.time.get_ticks()
잡은물고기 = 0
클릭횟수 = 10

물고기 = [물고기1, 물고기2]
전체물고기위치 = []
물고기정답위치 = []

def 게임종료():
    화면.blit(배경이미지, (0, 0))
    결과 = 폰트.render(f"총 {잡은물고기} 마리를 잡았어요!", True, (0, 0, 0))
    게임종료 = 폰트.render(f"게임 종료!", True, (0, 0, 0))
    화면.blit(게임종료, (230, 400))
    화면.blit(결과, (170, 550))
    pg.display.update()
    pg.time.delay(5000)
    quit()

def 게임판그리기():
    if len(전체물고기위치) == 0:
        for 가로 in range(70, 520, 90):
            for 세로 in range(370, 화면세로길이-30, 80):
                pg.draw.line(화면, (255, 255, 255), (70, 세로), (520, 세로), 3)
                pg.draw.line(화면, (255, 255, 255), (가로, 370), (가로, 화면세로길이-30), 3)
                전체물고기위치.append((가로+10, 세로+10))
        pg.draw.line(화면, (255, 255, 255), (70, 화면세로길이-30), (520, 화면세로길이-30), 3)
        pg.draw.line(화면, (255, 255, 255), (520, 370), (520, 화면세로길이-30), 3)
    else:
        for 가로 in range(70, 520, 90):
            for 세로 in range(370, 화면세로길이-30, 80):
                pg.draw.line(화면, (255, 255, 255), (70, 세로), (520, 세로), 3)
                pg.draw.line(화면, (255, 255, 255), (가로, 370), (가로, 화면세로길이-30), 3)
        pg.draw.line(화면, (255, 255, 255), (70, 화면세로길이-30), (520, 화면세로길이-30), 3)
        pg.draw.line(화면, (255, 255, 255), (520, 370), (520, 화면세로길이-30), 3)

def 물고기위치구하기(number: int,flag: int):
    global 물고기위치,물고기정답위치
    if flag == 0:
        물고기위치 = random.sample(전체물고기위치, number)
        for 위치 in range(number):
            랜덤물고기 = random.choice(물고기)
            물고기좌표 = 랜덤물고기.get_rect(topleft=(물고기위치[위치][0], 물고기위치[위치][1]))
            화면.blit(랜덤물고기, 물고기좌표)
            물고기정답위치.append(물고기좌표)
    else:
        물고기정답위치2 = []
        물고기위치 = random.sample(전체물고기위치, len(물고기정답위치))
        for 위치 in range(len(물고기정답위치)):
            랜덤물고기 = random.choice(물고기)
            물고기좌표 = 랜덤물고기.get_rect(topleft=(물고기위치[위치][0], 물고기위치[위치][1]))

            화면.blit(랜덤물고기, 물고기좌표)
            물고기정답위치2.append(물고기좌표)
                    
        물고기정답위치 = 물고기정답위치2

def 요소그리기():
    화면.blit(스코어바, (350, 2))
    화면.blit(시간바, (0, 10))

    시간 = 폰트.render(f"{경과시간} 초", True, (0, 0, 0))
    화면.blit(시간, (60, 28))
    물고기점수 = 폰트.render(f"{잡은물고기} 마리", True, (0, 0, 0))
    화면.blit(물고기점수, (450, 28))

게임판그리기()
물고기위치구하기(5,0)
pg.display.update()

while True:
    경과시간 = round((pg.time.get_ticks() - 시작시간) / 1000, 1)

    if 경과시간 == 10 or 클릭횟수 == 0:
        게임종료()

    요소그리기()
    pg.display.update()

    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()
        elif 이벤트.type == pg.MOUSEBUTTONDOWN:
            클릭횟수 -= 1
            마우스 = pg.mouse.get_pos()

            for 포인트 in 물고기정답위치:
                if 포인트.collidepoint(마우스):
                    물고기정답위치.remove(포인트)
                    잡은물고기 += 1
                    화면.blit(배경이미지, (0, 0))

                    게임판그리기()

                    if len(물고기정답위치) == 0:
                        #시작시간 = pg.time.get_ticks()

                        물고기위치구하기(5,0)
                        클릭횟수 = 10
                        continue

                    물고기위치구하기(len(물고기정답위치),1)
                    
                pg.display.update()

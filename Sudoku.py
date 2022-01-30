# 1.ゲームの準備をする
import pygame as pg, sys
import random
pg.init()
screen = pg.display.set_mode((800, 600))
## ブロックデータ
blocks = []
for zz in range(9):
    block=[]
    for yy in range(3):
        for xx in range(3):
            if yy==0:
                if xx==0:
                    if zz<=2:
                        block.append(pg.Rect(xx*30+50+(90-2)*zz, yy*30+50, 30, 30))
                    elif zz<=5:
                        block.append(pg.Rect(xx*30+50+(90-2)*(zz-3), yy*30+50+88, 30, 30))                       
                    else:
                        block.append(pg.Rect(xx*30+50+(90-2)*(zz-6), yy*30+50+88*2, 30, 30))
                else:
                    if zz<=2:
                        block.append(pg.Rect(xx*30+50-(xx+1)/2+(90-2)*zz, yy*30+50, 30, 30))
                    elif zz<=5:
                        block.append(pg.Rect(xx*30+50-(xx+1)/2+(90-2)*(zz-3), yy*30+50+88, 30, 30))                       
                    else:
                        block.append(pg.Rect(xx*30+50-(xx+1)/2+(90-2)*(zz-6), yy*30+50+88*2, 30, 30))             
            else:
                if xx==0:
                     if zz<=2:
                        block.append(pg.Rect(xx*30+50+(90-2)*zz, yy*30+50-(yy+1)/2, 30, 30))
                     elif zz<=5:
                        block.append(pg.Rect(xx*30+50+(90-2)*(zz-3),  yy*30+50-(yy+1)/2+88, 30, 30))                       
                     else:
                        block.append(pg.Rect(xx*30+50+(90-2)*(zz-6),  yy*30+50-(yy+1)/2+88*2, 30, 30)) 
                else:
                     if zz<=2:
                        block.append(pg.Rect(xx*30+50-(xx+1)/2+(90-2)*zz, yy*30+50-(yy+1)/2, 30, 30))
                     elif zz<=5:
                        block.append(pg.Rect(xx*30+50-(xx+1)/2+(90-2)*(zz-3),  yy*30+50-(yy+1)/2+88, 30, 30))                       
                     else:
                        block.append(pg.Rect(xx*30+50-(xx+1)/2+(90-2)*(zz-6),  yy*30+50-(yy+1)/2+88*2, 30, 30)) 
    blocks.append(block)
## ボタンデータ
replay_img = pg.image.load("samplesrc/part2/images/replaybtn.png")
## メインループで使う変数
pushFlag = False
page = 1 
score = 0
## btnを押したら、newpageにジャンプする
def button_to_jump(btn, newpage):
 global page, pushFlag
 # 4.ユーザーからの入力を調べる
 mdown = pg.mouse.get_pressed()
 (mx, my) = pg.mouse.get_pos()
 if mdown[0]:
   if btn.collidepoint(mx, my) and pushFlag == False:
      pg.mixer.Sound("samplesrc/part2/sounds/pi.wav").play()
      page = newpage
      pushFlag = True
   else:
      pushFlag = False
## ゲームステージ
def gamestage():
    # 3.画面を初期化する
    global page,score,blocks
    global vx, vy
    screen.fill(pg.Color("WHITE"))
    for block in blocks:
        for rect in block:
            pg.draw.rect(screen, pg.Color("BLACK"), rect, width=1)
def gamereset():
 global score ,blocks
 blocks = []
 for zz in range(9):
    block=[]
    for yy in range(3):
        for xx in range(3):
            if yy==0:
                if xx==0:
                    block.append(pg.Rect(xx*30+50*zz, yy*30+50*zz, 30, 30))
                else:
                    block.append(pg.Rect(xx*30-(50*zz/2)*(xx-1), yy*30+50*zz, 30, 30))               
            else:
                if xx==0:
                    block.append(pg.Rect(xx*30+50*zz, yy*30-(50*zz/2)*(yy-1), 30, 30))
                else:
                    block.append(pg.Rect(xx*30-(50*zz/2)*(xx-1),yy*30-(50*zz/2)*(yy-1), 30, 30))   
    blocks.append(block)
def gameclear():
 gamereset()
 screen.fill(pg.Color("GOLD"))
 font = pg.font.Font(None, 150)
 text = font.render("GAMECLEAR", True, pg.Color("RED"))
 screen.blit(text, (60, 200))
 btn1 = screen.blit(replay_img,(320, 480))
 # 5.絵を描いたり、判定したりする
 button_to_jump(btn1, 1)

# 2.この下をずっとループする
while True:
    if page == 1:
      gamestage()
    elif page == 2:
      gameclear()
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
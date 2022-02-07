# 1.ゲームの準備をする
from select import select
import pygame as pg, sys
import random
import itertools
from sqlalchemy import false
from sympy import re
import numpy as np
pg.init()
screen = pg.display.set_mode((800, 600))
##  問題データ
pro=np.array([
    [1,4,7,2,5,8,3,6,9],
    [2,5,8,3,6,9,4,7,1],
    [3,6,9,4,7,1,5,8,2],

    [4,7,1,5,8,2,6,9,3],
    [5,8,2,6,9,3,7,1,4],
    [6,9,3,7,1,4,8,2,5],
    
    [7,1,4,8,2,5,9,3,6],
    [8,2,5,9,3,6,1,4,7],
    [9,3,6,1,4,7,2,5,8]])
isvar=[ True for i in range(81)]
        
##  入力データ
print(pro)
board =[-1 for i in range(81)]
for yy in range(9):
    a=random.randint(0,4)
    x = random.sample(range(0,8),a)
    for i in x:
        board[yy*9+i]=pro[yy][i]
        isvar[yy*9+i]=False
print(board)
## ブロックデータ
i=0
block=[-1 for i in range(81)]
for zz in range(9):
    for yy in range(3):
        for xx in range(3):
            
            if yy==0:
                if xx==0:
                    if zz<=2:
                        block[i]=pg.Rect(xx*30+50+88*zz, yy*30+50, 30, 30)
                    elif zz<=5:
                        block[i]=pg.Rect(xx*30+50+88*(zz-3), yy*30+50+88, 30, 30)                    
                    else:
                        block[i]=pg.Rect(xx*30+50+88*(zz-6), yy*30+50+88*2, 30, 30)
                else:
                    if zz<=2:
                        block[i]=pg.Rect(xx*30+50-(xx+1)/2+88*zz, yy*30+50, 30, 30)
                    elif zz<=5:
                        block[i]=pg.Rect(xx*30+50-(xx+1)/2+88*(zz-3), yy*30+50+88, 30, 30)                      
                    else:
                        block[i]=pg.Rect(xx*30+50-(xx+1)/2+88*(zz-6), yy*30+50+88*2, 30, 30)           
            else:
                if xx==0:
                     if zz<=2:
                        block[i]=pg.Rect(xx*30+50+88*zz, yy*30+50-(yy+1)/2, 30, 30)
                     elif zz<=5:
                        block[i]=pg.Rect(xx*30+50+88*(zz-3),  yy*30+50-(yy+1)/2+88, 30, 30)                
                     else:
                        block[i]=pg.Rect(xx*30+50+88*(zz-6),  yy*30+50-(yy+1)/2+88*2, 30, 30)
                else:
                     if zz<=2:
                        block[i]=pg.Rect(xx*30+50-(xx+1)/2+88*zz, yy*30+50-(yy+1)/2, 30, 30)
                     elif zz<=5:
                        block[i]=pg.Rect(xx*30+50-(xx+1)/2+88*(zz-3),  yy*30+50-(yy+1)/2+88, 30, 30)                   
                     else:
                        block[i]=pg.Rect(xx*30+50-(xx+1)/2+88*(zz-6),  yy*30+50-(yy+1)/2+88*2, 30, 30) 
            i+=1
#数字盤
input=[]
for yy in range(3):
        for xx in range(3):
            if yy==0:
                if xx==0:
                        input.append(pg.Rect(xx*30+50, yy*30+50+300, 30, 30))
                else:
                        input.append(pg.Rect(xx*30+50-(xx+1)/2, yy*30+50+300, 30, 30))             
            else:
                if xx==0:
                        input.append(pg.Rect(xx*30+50,  yy*30+50-(yy+1)/2+300, 30, 30)) 
                else:
                        input.append(pg.Rect(xx*30+50-(xx+1)/2,  yy*30+50-(yy+1)/2+300, 30, 30)) 
## ボタンデータ
replay_img = pg.image.load("samplesrc/part2/images/replaybtn.png")
## メインループで使う変数
pushFlag = False
page = 1 
score = 0
sel=pg.rect
selin=pg.rect
selnum=0
presel=0
tnum=0
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
    global page,score,block,sel,selin,board,selnum,tnum,presel,isvar  
    screen.fill(pg.Color("WHITE"))
    (mx, my) = pg.mouse.get_pos()
    buttons= pg.mouse.get_pressed()
    index=1
    pg.draw.rect(screen,(135,206,235),pg.Rect(600,390,70,50))
    font = pg.font.Font(None, 30)
    text = font.render("done!", True, pg.Color("BLACK"))
    screen.blit(text, (607, 405))  
    if (mx>=600 and mx<600+70 and my>=390 and my<390+50 and buttons[0]):
        isdone()
    for i     in input:
        pg.draw.rect(screen, pg.Color("BLACK"), i, width=1)
        if (my>=i.y and my<i.y+30 and mx>=i.x and mx<i.x+30 and buttons[0]):
                selin=i
                if selin==presel:
                    tnum+=1
                presel=i
        if selin==i:
                pg.draw.rect(screen,(165, 197, 246), i)
                if selin!=presel:
                    tnum==0
                selnum=index
        else:
                 pg.draw.rect(screen,pg.Color("WHITE"), i)
        font = pg.font.Font(None, 30)
        text = font.render(str(index), True, pg.Color("BLACK"))
        screen.blit(text, (i.x+9, i.y+7))     
        pg.draw.rect(screen, pg.Color("BLACK"), i, width=1)   
        index+=1
    
    for q , rect in enumerate(block):
        if q==81: break
        if isvar[q]==False:
                pg.draw.rect(screen,(165, 197, 246), rect)
                pg.draw.rect(screen, pg.Color("BLACK"), rect, width=1)
                font = pg.font.Font(None, 30)
                text = font.render(str(board[q]), True, pg.Color("BLACK"))   
        if (my>=rect.y and my<rect.y+30 and mx>=rect.x and mx<rect.x+30 and buttons[0] and isvar[q]):
            sel=rect
            tnum=0
        if sel==rect:
                pg.draw.rect(screen, pg.Color("GOLD"), rect)
                if tnum!=0:
                     board[q]=selnum
                     text = font.render(str(selnum), True, pg.Color("BLACK"))
                     screen.blit(text, (rect.x+9, rect.y+7))
                elif tnum==0 and board[q]!=-1:
                     text = font.render(str(board[q]), True, pg.Color("BLACK"))
                     screen.blit(text, (rect.x+9, rect.y+7))
                pg.draw.rect(screen, pg.Color("BLACK"), rect, width=1)   
        else:
                pg.draw.rect(screen, pg.Color("BLACK"), rect, width=1)
                if not(board[q]==-1):
                   text = font.render(str(board[q]), True, pg.Color("BLACK"))
                   screen.blit(text, (rect.x+9, rect.y+7))
        
def gamereset():
 global score,block,sel,selin,board,selnum,tnum,presel,isvar  
 score = 0
 sel=pg.rect
 selin=pg.rect
 selnum=0
 presel=0
 tnum=0
 isvar=[True for i in range(81)]
 board =[-1 for i in range(81)]
 pro=np.array([
    [1,4,7,2,5,8,3,6,9],
    [2,5,8,3,6,9,4,7,1],
    [3,6,9,4,7,1,5,8,2],

    [4,7,1,5,8,2,6,9,3],
    [5,8,2,6,9,3,7,1,4],
    [6,9,3,7,1,4,8,2,5],
    
    [7,1,4,8,2,5,9,3,6],
    [8,2,5,9,3,6,1,4,7],
    [9,3,6,1,4,7,2,5,8]])
 for yy in range(9):
    a=random.randint(0,4)
    x = random.sample(range(0,8),a)
    for i in x:
        board[yy*9+i]=pro[yy][i]
        isvar[yy*9+i]=False
def gameclear():
 gamereset()
 screen.fill(pg.Color("GOLD"))
 font = pg.font.Font(None, 150)
 text = font.render("GAMECLEAR", True, pg.Color("RED"))
 screen.blit(text, (60, 200))
 btn1 = screen.blit(replay_img,(320, 480))
 # 5.絵を描いたり、判定したりする
 button_to_jump(btn1, 1)
 # クリア判定
def isdone():
    global board,pro,page
    isfill=True
    score=0
    for i in range(81):
        if board[i]==-1:
            isfill=False
            font = pg.font.Font(None, 30)
            text = font.render("Fill all the squares!", True, pg.Color("RED"))
            screen.blit(text, (607, 305))
            break
    if isfill:
        for i in range(81):
            if board[i]!=pro[i//9][i%9]:
                score+=1
        font = pg.font.Font(None, 30)
        text = font.render("You got "+str(score)+" wrong.", True, pg.Color("RED"))
        screen.blit(text, (607, 305))
        if score==0:
            page=2

    
    


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
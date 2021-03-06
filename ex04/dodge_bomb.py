import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm

def colend():
    tkm.showwarning("ドンマイ","当たってしまいましたね…")


def main():
    #練習１　スクリーン
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ!!こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))  #Surface
    screen_rct = screen_sfc.get_rect()              #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")     #Surface
    bgimg_rct = bgimg_sfc.get_rect()               #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    #練習3　：こうかとん
    kkimg_sft = pg.image.load("fig/3.png")         #Surface
    kkimg_sft = pg.transform.rotozoom(kkimg_sft, 0, 2.0)       #Surface
    kkimg_rct = kkimg_sft.get_rect()               #Rect
    kkimg_rct.center = 900, 400      #こうかとん表示

    #練習5　：爆弾
    bmimg_sfc = pg.Surface((20,20)) #Surface
    bmimg_sfc.set_colorkey((0, 0, 0))  #黒い部分を透明
    pg.draw.rect(bmimg_sfc, (128, 0, 128), (10, 10, 10, 10))
    bmimg_rct = bmimg_sfc.get_rect() #Rect
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)


    vx, vy = +1, +1 #練習6

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)  #Surfaceに貼り付け
        
        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #練習4
        key_states = pg.key.get_pressed() #辞書
        if key_states[pg.K_UP] or key_states[pg.K_w]   == True: kkimg_rct.centery -=1
        if key_states[pg.K_DOWN] or key_states[pg.K_s] == True: kkimg_rct.centery +=1
        if key_states[pg.K_LEFT] or key_states[pg.K_a] == True: kkimg_rct.centerx -=1
        if key_states[pg.K_RIGHT] or key_states[pg.K_d] == True: kkimg_rct.centerx +=1

        if check_bound(kkimg_rct, screen_rct) != (1,1): #領域外ならば
            if key_states[pg.K_UP] or key_states[pg.K_w]   == True: kkimg_rct.centery +=1
            if key_states[pg.K_DOWN] or key_states[pg.K_s] == True: kkimg_rct.centery -=1
            if key_states[pg.K_LEFT] or key_states[pg.K_a] == True: kkimg_rct.centerx +=1
            if key_states[pg.K_RIGHT] or key_states[pg.K_d] == True: kkimg_rct.centerx -=1

        screen_sfc.blit(kkimg_sft, kkimg_rct)  #Surfaceに貼り付け

        #練習5
        screen_sfc.blit(bmimg_sfc, bmimg_rct)

        #練習6
        bmimg_rct.move_ip(vx, vy)
        #練習7
        yoko, tate = check_bound(bmimg_rct, screen_rct)
        vx *= yoko
        vy *= tate

        #練習8
        if kkimg_rct.colliderect(bmimg_rct):  #衝突判定
            a=pg.time.get_ticks()/1000
            tkm.showinfo("時間",f"{a}秒でした。")
            colend()
            return


        pg.display.update()  #描画を更新
        clock.tick(1000)

#練習7
def check_bound(rct, scr_rct):   #rctはこうかとんと爆弾のRect、scr_rctはスクリーンのRect
    yoko, tate = +1, +1
    if rct.left < scr_rct.left or scr_rct.right  < rct.right  : yoko = -1 #領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom : tate = -1 #領域外
    return yoko, tate 


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    pg.init()
    main()
    pg.quit()
    sys.exit()


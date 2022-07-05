import pygame as pg
import sys

def main():
    #練習１
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ!!こうかとん")
    screen_sft = pg.display.set_mode((1600, 900))  #Surface
    sreen_rct = screen_sft.get_rect()              #Rect
    bgimg_sft = pg.image.load("fig/pg_bg.jpg")     #Surface
    bgimg_rct = bgimg_sft.get_rect()               #Rect
    screen_sft.blit(bgimg_sft, bgimg_rct)

    #練習3
    kkimg_sft = pg.image.load("fig/6.png")         #Surface
    kkimg_sft = pg.transform.rotozoom(kkimg_sft, 0, 2.0)       #Surface
    kkimg_rct = kkimg_sft.get_rect()               #Rect
    kkimg_rct.center = 900, 400      #こうかとん表示

    while True:
        screen_sft.blit(bgimg_sft, bgimg_rct)  #Surfaceに貼り付け
        
        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #練習4
        key_states = pg.key.get_pressed() #辞書
        if key_states[pg.K_UP]    == True: kkimg_rct.centery -=1
        if key_states[pg.K_DOWN]  == True: kkimg_rct.centery +=1
        if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -=1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx +=1

        screen_sft.blit(kkimg_sft, kkimg_rct)  #Surfaceに貼り付け

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()


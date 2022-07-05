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

    #練習２
    kkimg_sft = pg.image.load("fig/6.png")         #Surface
    kkimg_sft = pg.transform.rotozoom(kkimg_sft, 0, 2.0)       #Surface
    kkimg_rct = kkimg_sft.get_rect()               #Rect
    kkimg_rct.center = 900, 400      #こうかとん表示

    while True:
        screen_sft.blit(bgimg_sft, bgimg_rct)
        screen_sft.blit(kkimg_sft, kkimg_rct)

        #練習
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()


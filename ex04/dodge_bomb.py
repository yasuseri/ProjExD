import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ!!こうかとん")
    screen_sft = pg.display.set_mode((1600, 900))  #surface
    sreen_rct = screen_sft.get_rect()              #rect
    bgimg_sft = pg.image.load("fig/pg_bg.jpg")      #surface
    bgimg_rct = bgimg_sft.get_rect()               #rect
    screen_sft.blit(bgimg_sft, bgimg_rct)


    while True:
        screen_sft.blit(bgimg_sft, bgimg_rct)

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


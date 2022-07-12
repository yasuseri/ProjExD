import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm

class kill:    #ゲームオーバーしたときの表示
    def __init__(self):
        tkm.showwarning("ドンマイ","当たってしまいましたね…")   #衝突後のメッセージ表示


class Screen:   #screenをだす
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)       # Surface
        self.rct = self.sfc.get_rect()           # Rect
        self.bgi_sfc = pg.image.load(image)      # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()   # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy   #こうかとん表示

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP] or key_states[pg.K_w]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN] or key_states[pg.K_s]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT] or key_states[pg.K_a]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT] or key_states[pg.K_d]: 
            self.rct.centerx += 1
        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP] or key_states[pg.K_w]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN] or key_states[pg.K_s]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT] or key_states[pg.K_a]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT] or key_states[pg.K_d]:
                self.rct.centerx -= 1
        self.blit(scr)
    
    def attack(self):
        return Shot(self,(+1,0))


class Bomb:   #爆弾１
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0))   #黒い部分を透明化
        pg.draw.circle(self.sfc, color, (size, size), size)   #円形の爆弾を作る
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)   #スタート位置をランダムにする
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)   #爆弾移動
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)   #こうかとんと爆弾が画面外に出ないようにする
        self.vx *= yoko
        self.vy *= tate
        # 練習5
        self.blit(scr)


class Bomb2:   #爆弾２
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc2 = pg.Surface((2*size, 2*size)) # Surface
        self.sfc2.set_colorkey((0, 0, 0))   #黒い部分を透明化
        pg.draw.rect(self.sfc2, color, (size, size, size, size))   #円形の爆弾を作る
        self.rct2 = self.sfc2.get_rect() # Rect
        self.rct2.centerx = random.randint(0, scr.rct.width)   #スタート位置をランダムにする
        self.rct2.centery = random.randint(0, scr.rct.height)
        self.vx2, self.vy2 = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc2, self.rct2)

    def update(self, scr: Screen):
        # 練習6
        self.rct2.move_ip(self.vx2, self.vy2)   #爆弾移動
        # 練習7
        yoko, tate = check_bound(self.rct2, scr.rct)   #こうかとんと爆弾が画面外に出ないようにする
        self.vx2 *= yoko
        self.vy2 *= tate
        # 練習5
        self.blit(scr)


class Bomb3:   #爆弾３
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc3 = pg.Surface((2*size, 2*size)) # Surface
        self.sfc3.set_colorkey((0, 0, 0))   #黒い部分を透明化
        pg.draw.rect(self.sfc3, color, (size, size, size, size))   #円形の爆弾を作る
        self.rct3 = self.sfc3.get_rect() # Rect
        self.rct3.centerx = random.randint(0, scr.rct.width)   #スタート位置をランダムにする
        self.rct3.centery = random.randint(0, scr.rct.height)
        self.vx3, self.vy3 = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc3, self.rct3)

    def update(self, scr: Screen):
        # 練習6
        self.rct3.move_ip(self.vx3, self.vy3)   #爆弾移動
        # 練習7
        yoko, tate = check_bound(self.rct3, scr.rct)   #こうかとんと爆弾が画面外に出ないようにする
        self.vx3 *= yoko
        self.vy3 *= tate
        # 練習5
        self.blit(scr)


class Shot:  #ビーム
    def __init__(self, chr: Bird, vxy):
        self.sfc = pg.image.load("fig/beam.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.1) # Surface
        self.rct = self.sfc.get_rect()
        self.rct.midleft = chr.rct.center
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)

        self.blit(scr)


def main():
    clock = pg.time.Clock()

    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    
    kkt = Bird("fig/6.png", 2.0, (900, 400))   #各クラスの呼び出し

    
    bkd = Bomb((255, 0, 0), 10, (+1,+1), scr)


    bkb2 = Bomb2((128, 0, 128), 20, (+2,+2), scr)


    bkb3 = Bomb3((128, 0, 0), 20, (+3,+3), scr)

    beam = Shot(kkt,(+1,+0)) 

    while True:
        scr.blit()   #Surfaceに貼り付け
        #screen_sfc.blit(bgimg_sfc, bgimg_rct)

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            if event.type == pg.KEYDOWN and event.key ==pg.K_SPACE:
                beam = kkt.attack()

        
        kkt.update(scr)   #Surfaceに貼り付け

        bkd.update(scr)

        bkb2.update(scr)

        bkb3.update(scr)  

        beam.update(scr)


        if kkt.rct.colliderect(bkd.rct):   #当たり判定
            a=pg.time.get_ticks()/1000
            tkm.showinfo("時間",f"{a}秒でした。")   #時間表示
            kill()   #メッセージ表示関数を呼び出す
            return
        
        if kkt.rct.colliderect(bkb2.rct2):
            a=pg.time.get_ticks()/1000
            tkm.showinfo("時間",f"{a}秒でした。")   #時間表示
            kill()   #メッセージ表示関数を呼び出す
            return
        
        if kkt.rct.colliderect(bkb3.rct3):
            a=pg.time.get_ticks()/1000
            tkm.showinfo("時間",f"{a}秒でした。")   #時間表示
            kill()   #メッセージ表示関数を呼び出す
            return
        
        if beam.rct.colliderect(bkd.rct):   #ビームの当たり判定　
            a=pg.time.get_ticks()/1000
            tkm.showinfo("時間",f"{a}秒でした。")   #時間表示
            return

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    root = tk.Tk()   #不要なメッセージの削除
    root.withdraw()
    pg.init()
    main()
    pg.quit()
    sys.exit()
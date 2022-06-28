import tkinter as tk
import maze_maker as mm


def key_down(event):
    global key   #グローバル変数
    key = event.keysym

def key_up(event):
    global key   #グローバル変数
    key = ""


def main_proc():
    global cx, cy, mx, my   #グローバル変数
    delta = {   #キー：押されているキーkey/値：移動幅リスト[x,y]
            "Up"    : [0, -1], 
            "Down"  : [0, +1],
            "Left"  : [-1, 0],
            "Right" : [+1, 0],
            "a"     : [-1, 0],
            "w"     : [0, -1],
            "s"     : [0, +1],
            "d"     : [+1, 0],
    }
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:  #もし移動先が床なら
            my, mx = my+delta[key][1], mx+delta[key][0]
    except:  #もし移動先が壁なら
        pass

    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    if cx == 1350:
        if cy == 750:
            tori = tk.PhotoImage(file="fig/3.png")
            mx, my = 1, 1
            cx, cy = mx*100+50, my*100+50
            canvas.create_image(cx,cy, image=tori, tag='tori')
            
    else:
        pass
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")   #タイトルを書く

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")   #背景色とウインドウを生成
    canvas.pack()


    maze_bg = mm.make_maze(15, 9)   #1が壁,0が床のリストを生成
    mm.show_maze(canvas, maze_bg)   #canvasにmaze_bgを書く
    #print(maze_bg)

    tori = tk.PhotoImage(file="fig/3.png")   #5のこうかとんを使う
    st = tk.PhotoImage(file="fig/5.png")   #スタート地点にこうかとん
    go = tk.PhotoImage(file="fig/4.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50  #初期位置
    
    canvas.create_image(cx, cy, image=tori, tag="tori")
    canvas.create_image(150, 150, image=st, tag="st")
    canvas.create_image(1350, 750, image=go, tag="go")
    

    key = ""



    root.bind("<KeyPress>", key_down)   #キーが押されたら…
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()  #ウインドウを表示




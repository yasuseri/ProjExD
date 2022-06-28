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
    }
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:  #もし移動先が床なら
            my, mx = my+delta[key][1], mx+delta[key][0]
    except:
        pass

    #mx+delta[key][0], my+delta[key][1]
    #if maze_bg[mx+delta[key][0]][my+delta[key][1]] == 1:  #もし移動先が床なら
    #    my, mx = my+delta[key][1], mx+delta[key][0]
    #if key == "Up"    : my-=1
    #if key == "Down"  : my+=1
    #if key == "Left"  : mx-=1
    #if key == "Right" : mx+=1
    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")   #タイトルを書く

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")   #背景色とウインドウを生成
    canvas.pack()
    maze_bg = mm.make_maze(15, 9)   #1が壁,0が床のリストを生成
    mm.show_maze(canvas, maze_bg)   #canvasにmaze_bgを書く
    #print(maze_bg)

    tori = tk.PhotoImage(file="fig/6.png")   #６のこうかとんを使う
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50  #初期位置
    
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""

    root.bind("<KeyPress>", key_down)   #キーが押されたら…
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()  #ウインドウを表示




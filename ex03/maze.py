import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key   #グローバル変数
    key = event.keysym

def key_up(event):
    global key   #グローバル変数
    key = ""

def main_proc():
    global cx, cy   #グローバル変数
    #delta = {   #キー：押されているキーkey/値：移動幅リスト[x,y]
    #        ""      : [0,   0],
    #        "Up"    : [0, -20], 
    #        "Down"  : [0, +20],
    #        "Left"  : [-20, 0],
    #        "Right" : [+20, 0],
    #        }
    #cx, cy = cx+delta[key][0], cy+delta[key][1]
    if key == "Up"    : cy-=20
    if key == "Down"  : cy+=20
    if key == "Left"  : cx-=20
    if key == "Right" : cx+=20
    if key == ""      : cx+=0
    
    canvas.coords("tori", cx, cy)
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")   #タイトルを書く

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")   #背景色とウインドウを生成
    canvas.pack()
    maze_bg = mm.make_maze(15, 9)   #1が壁,0が床のリストを生成
    print(maze_bg)

    tori = tk.PhotoImage(file="fig/6.png")   #６のこうかとんを使う
    cx, cy = 300, 400  #初期位置
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""

    root.bind("<KeyPress>", key_down)   #キーが押されたら…
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()  #ウインドウを表示




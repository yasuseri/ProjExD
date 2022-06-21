import math
import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    btn = event.widget
    num = btn["text"]
    eqn = entry.get()
    if num == "=":   #計算結果を出す
        res = eval(eqn)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    
    elif num == "sin":   #数値を入力後にsinの値を返す
        res_sin1 = math.sin(math.radians(int(eqn)))
        entry.delete(0, tk.END)
        res_sin2=round(res_sin1, 3)
        entry.insert(tk.END, res_sin1)

    elif num == "cos":   #数値を入力後にcosの値を返す
        res_cos = math.cos(math.radians(int(eqn)))
        entry.delete(0, tk.END)
        res_cos1=round(res_cos, 3)
        entry.insert(tk.END, res_cos1)
    
    elif num == "tan":   #数値を入力後にtanの値を返す
        res_tan = math.tan(math.radians(int(eqn)))
        entry.delete(0, tk.END)
        res_tan1=round(res_tan, 3)
        entry.insert(tk.END, res_tan1)

    elif num == "C":   #一文字ずつ消えるデリートキー
        entry.delete(len(eqn)-1, tk.END)

    elif num == "AC":   #すべての文字を消すキー
        entry.delete(0, tk.END)

    elif num == "%":  #％表示する
        eqn_a=int(eqn)/100
        entry.delete(0, tk.END)
        entry.insert(tk.END, eqn_a)

    else:
        entry.insert(tk.END,num)    #それぞれのボタンを電卓に表示



if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("300x600")   
    root.title("電卓")   #名前を付ける


    entry = tk.Entry(root, justify="right", width=10, font=("times New Romen", 40))
    entry.grid(row = 0, column = 0, columnspan = 8)   #テキスト入力欄を設定


    r, c= 1, 0   #列番号と行番号
    for i, num in enumerate([7, 8, 9,"/", 4, 5, 6,"*" , 3, 2 ,1 ,"-", 0, "00","000","+","%",".", "C","=","sin","cos","tan","AC"]):  #表示ボタンを設定
        btn = tk.Button(root, text=f"{num}", width=4, height=2,
              font=("Time New Roman", 30))    #それぞれのボタンを生成

        btn.bind("<1>", button_click)    #左クリックで反応
        btn.grid(row = r, column = c)

        c += 1
        if (i+1)%4 == 0:
            r += 1
            c = 0


    root.mainloop()   #ウインドウを表示
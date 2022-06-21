import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    else:
        #tkm.showinfo("", f"{num}のボタンがクリックされました")
        entry.insert(tk.END,num)    #それぞれのボタンを電卓に表示



if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("300x600")   #フィールドを生成
    root.title("普通の電卓")   #名前を付ける


    entry = tk.Entry(root, justify="right", width=10, font=("times New Romen", 40))
    entry.grid(row = 0, column = 0, columnspan = 3)   #テキスト入力欄を設定


    r, c= 1, 0   #列番号と行番号
    for i, num in enumerate([9, 8, 7, 6, 5, 4, 3, 2 ,1 , 0, "+", "="]):
        btn = tk.Button(root, text=f"{num}", width=4, height=2,
              font=("Time New Roman", 30))    #それぞれのボタンを生成

        btn.bind("<1>", button_click)    #左クリックで反応
        btn.grid(row=r, column=c)

        c += 1
        if (i+1)%3 == 0:
            r += 1
            c = 0


    root.mainloop()   #ウインドウを表示